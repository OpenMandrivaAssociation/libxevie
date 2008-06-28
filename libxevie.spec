%define major 1
%define libname %mklibname xevie %{major}
%define develname %mklibname xevie -d
%define staticdevelname %mklibname xevie -d -s

Name: libxevie
Summary:  X Event Interceptor Library
Version: 1.0.2
Release: %mkrel 5
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXevie-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

BuildRoot: %{_tmppath}/%{name}-root

%description
X Event Interceptor Library.

#-----------------------------------------------------------

%package -n %{libname}
Summary: X Event Interceptor Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
X Event Interceptor Library.

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} >= %{version}-%{release}
Requires: x11-proto-devel >= 1.0.0
Provides: %{name}-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0
Obsoletes: %mklibname xevie 1 -d

%description -n %{develname}
Development files for %{name}.

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXevie.so
%{_libdir}/libXevie.la
%{_libdir}/pkgconfig/xevie.pc
%{_includedir}/X11/extensions/Xevie.h
%{_mandir}/man3/Xevie*.3*

#-----------------------------------------------------------

%package -n %{staticdevelname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}
Provides: %{name}-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0
Obsoletes: %mklibname xevie 1 -d -s

%description -n %{staticdevelname}
Static development files for %{name}.

%files -n %{staticdevelname}
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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXevie.so.%{major}*
