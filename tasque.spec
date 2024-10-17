Summary: A simple task management app (TODO list) for the Linux Desktop
Name: tasque
Version: 0.1.9
Release: %mkrel 3
Source0: http://ftp.gnome.org/pub/GNOME/sources/tasque/0.1/%{name}-%{version}.tar.gz
License: MIT
Group: Graphical desktop/GNOME
Url: https://live.gnome.org/Tasque
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: pkgconfig(glade-sharp-2.0)
BuildRequires: pkgconfig(gnome-sharp-2.0)
BuildRequires: pkgconfig(gtk-sharp-2.0)
BuildRequires: pkgconfig(evolution-sharp)
BuildRequires: pkgconfig(ndesk-dbus-glib-1.0)
BuildRequires: pkgconfig(notify-sharp)
BuildRequires: intltool

%description
Tasque is a simple task management app (TODO list) for the Linux Desktop. 

%prep
%setup -q -n%name-%version

%build
%configure2_5x --enable-standard-backends
%make

%install
rm -fr %buildroot
%makeinstall_std

%find_lang %name --with-gnome

%clean
rm -fr %buildroot

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_libdir}/pkgconfig/*.pc
%{_libexecdir}/%name/Tasque.exe
%{_libexecdir}/%name/Tasque.exe.config
%{_libexecdir}/%name/Tasque.exe.mdb
%{_libexecdir}/%name/RtmNet.dll
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/pixmaps/*
%{_datadir}/dbus-1/services/org.gnome.Tasque.service


%changelog
* Wed Dec 14 2011 Götz Waschk <waschk@mandriva.org> 0.1.9-3mdv2012.0
+ Revision: 740998
- rebuild for gtk+ packaging breakage

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.9-2mdv2011.0
+ Revision: 615135
- the mass rebuild of 2010.1 packages

* Wed Feb 17 2010 Funda Wang <fwang@mandriva.org> 0.1.9-1mdv2010.1
+ Revision: 507092
- update desc
- import tasque


