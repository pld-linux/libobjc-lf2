
%define		libf_objc_makeflags	-s
%define		__source		.

Summary:	GNUstep Objective C runtime.
Name:		libobjc-lf2
Version:	lf2
Release:	95.3
Vendor:		http://www.gnustep.org
License:	GPL
Group:		Development/Libraries
AutoReqProv:	off
Source0:	http://download.opengroupware.org/sources/trunk/%{name}-trunk-latest.tar.gz
#Patch0:
URL:		http://www.opengroupware.org

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildPreReq:	gnustep-make

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gcc-objc
BuildRequires:	gnustep-make >= 1.10.0


%description
GNUstep Objective C runtime.

%package devel
Summary:	The header files for the objc library.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires: 	gnustep-make
AutoReqProv:	off

%description devel
GNUstep Objective C development package.

%prep
%setup -q -n libobjc-lf2

%build
%{__source} %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
%{__make} %{libf_objc_makeflags} all


%install
rm -rf $RPM_BUILD_ROOT
%{__source} %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
%{__make} %{libf_objc_makeflags} GNUSTEP_INSTALLATION_DIR=${RPM_BUILD_ROOT}%{_libdir}/GNUstep/System install

install -d ${RPM_BUILD_ROOT}%{_libdir}
mv ${RPM_BUILD_ROOT}%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu/libobjc*.so.lf2* ${RPM_BUILD_ROOT}%{_libdir}/


%post
if [ $1 = 1 ]; then
  if [ -e %{_libdir}/libobjc_d.so.lf2 ]; then
    cd %{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu
    ln -s %{_libdir}/libobjc_d.so.lf2
  fi
  if [ -e %{_libdir}/libobjc.so.lf2 ]; then
    cd %{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu
    ln -s %{_libdir}/libobjc.so.lf2
  fi
  if [ -d %{_sysconfdir}/ld.so.conf.d ]; then
    echo "%{_libdir}" > %{_sysconfdir}/ld.so.conf.d/libobjc-lf2.conf
  elif [ ! "`grep '%{_libdir}' %{_sysconfdir}/ld.so.conf`" ]; then
    echo "%{_libdir}" >> %{_sysconfdir}/ld.so.conf
  fi
  /sbin/ldconfig
fi


%postun
if [ $1 = 0 ]; then
  if [ -h %{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu/libobjc_d.so.lf2 ]; then
    rm -f %{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu/libobjc_d.so.lf2
  fi
  if [ -h %{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu/libobjc.so.lf2 ]; then
    rm -f %{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu/libobjc.so.lf2
  fi
  if [ -e %{_sysconfdir}/ld.so.conf.d/libobjc-lf2.conf ]; then
    rm -f %{_sysconfdir}/ld.so.conf.d/libobjc-lf2.conf
  fi
  /sbin/ldconfig
fi


%clean
rm -fr ${RPM_BUILD_ROOT}


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libobjc*.so.lf2*
%files devel
%defattr(644,root,root,755)
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/objc
%attr(755,root,root) %{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu/libobjc*.so
