%define libxevie %mklibname xevie 1
Name: libxevie
Summary:  X Event Interceptor Library
Version: 1.0.1
Release: %mkrel 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXevie-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X Event Interceptor Library

#-----------------------------------------------------------

%package -n %{libxevie}
Summary: X Event Interceptor Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxevie}
X Event Interceptor Library

#-----------------------------------------------------------

%package -n %{libxevie}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxevie} >= %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxevie-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxevie}-devel
Development files for %{name}

%pre -n %{libxevie}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxevie}-devel
%defattr(-,root,root)
%{_libdir}/libXevie.so
%{_libdir}/libXevie.la
%{_libdir}/pkgconfig/xevie.pc
%{_includedir}/X11/extensions/Xevie.h
%{_mandir}/man3/Xevie*.3x.bz2

#-----------------------------------------------------------

%package -n %{libxevie}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxevie}-devel = %{version}
Provides: libxevie-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxevie}-static-devel
Static development files for %{name}

%files -n %{libxevie}-static-devel
%defattr(-,root,root)
%{_libdir}/libXevie.a

#-----------------------------------------------------------

%prep
%setup -q -n libXevie-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxevie}
%defattr(-,root,root)
%{_libdir}/libXevie.so.1
%{_libdir}/libXevie.so.1.0.0


