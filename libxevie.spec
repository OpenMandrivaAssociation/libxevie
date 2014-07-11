%define major 1
%define libname %mklibname xevie %{major}
%define devname %mklibname xevie -d

Summary:	X Event Interceptor Library
Name:		libxevie
Version:	1.0.3
Release:	12
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXevie-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
X Event Interceptor Library.

%package -n %{libname}
Summary:	X Event Interceptor Library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
X Event Interceptor Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%pre -n %{devname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%prep
%setup -qn libXevie-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXevie.so.%{major}*

%files -n %{devname}
%{_libdir}/libXevie.so
%{_libdir}/pkgconfig/xevie.pc
%{_includedir}/X11/extensions/Xevie.h
%{_mandir}/man3/Xevie*.3*

