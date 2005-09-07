%define		libf_objc_makeflags	-s
%define		trunkdate		200508291710

Summary:	GNUstep Objective C runtime
Summary(pl):	Biblioteka uruchomieniowa Objective C dla GNUstepa
Name:		libobjc-lf2
Version:	r124       
Release:	1
Vendor:		http://www.gnustep.org/
License:	GPL
Group:		Libraries
Source0:	http://download.opengroupware.org/sources/trunk/%{name}-trunk-%{version}-%{trunkdate}.tar.gz
# Source0-md5:	b470016fe3c7011a33dd9778af130118
URL:		http://www.opengroupware.org/
#AutoReqProv:	off
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gcc-objc
BuildRequires:	gnustep-make-devel >= 1.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNUstep Objective C runtime.

%description -l pl
Biblioteka uruchomieniowa Objective C dla GNUstepa.

%package devel
Summary:	The header files for the ObjC library
Summary(pl):	Pliki nag³ówkowe biblioteki ObjC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires: 	gnustep-make-devel
#AutoReqProv:	off

%description devel
GNUstep Objective C development package.

%description devel -l pl
Pakiet programistyczny GNUstep Objective C.

%prep
%setup -q -n libobjc-lf2

%build
. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
%{__make} %{libf_objc_makeflags} all

%install
rm -rf $RPM_BUILD_ROOT

. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
%{__make} %{libf_objc_makeflags} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_libdir}/GNUstep/System

install -d $RPM_BUILD_ROOT%{_libdir}
mv $RPM_BUILD_ROOT%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu/libobjc*.so.lf2* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = "1" ]; then
	if [ -e %{_libdir}/libobjc_d.so.lf2 ]; then
		cd %{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu
		ln -sf %{_libdir}/libobjc_d.so.lf2
	fi
	if [ -e %{_libdir}/libobjc.so.lf2 ]; then
		cd %{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu
		ln -sf %{_libdir}/libobjc.so.lf2
	fi
fi
/sbin/ldconfig

%postun
if [ "$1" = "0" ]; then
	if [ -h %{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu/libobjc_d.so.lf2 ]; then
		rm -f %{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu/libobjc_d.so.lf2
	fi
	if [ -h %{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu/libobjc.so.lf2 ]; then
		rm -f %{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu/libobjc.so.lf2
	fi
	if [ -e %{_sysconfdir}/ld.so.conf.d/libobjc-lf2.conf ]; then
		rm -f %{_sysconfdir}/ld.so.conf.d/libobjc-lf2.conf
	fi
fi
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libobjc*.so.lf2*

%files devel
%defattr(644,root,root,755)
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/objc
%attr(755,root,root) %{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu/libobjc*.so
