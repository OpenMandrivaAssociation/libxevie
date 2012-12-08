%define major 1
%define libname %mklibname xevie %{major}
%define develname %mklibname xevie -d
%define staticdevelname %mklibname xevie -d -s

Name: libxevie
Summary:  X Event Interceptor Library
Version: 1.0.3
Release: %mkrel 4
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


%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 660299
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 591817
- new release

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-7mdv2010.1
+ Revision: 520965
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-6mdv2010.0
+ Revision: 425891
- rebuild

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-5mdv2009.0
+ Revision: 229750
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Tue Jan 22 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-3mdv2008.1
+ Revision: 156502
- Updated BuildRequires and resubmit package.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jul 17 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-2mdv2008.0
+ Revision: 52772
- correct scriplets

* Mon Jul 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 52756
- new version
- new devel library policy
- spec file clean


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

