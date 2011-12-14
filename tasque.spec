Summary: A simple task management app (TODO list) for the Linux Desktop
Name: tasque
Version: 0.1.9
Release: %mkrel 3
Source0: http://ftp.gnome.org/pub/GNOME/sources/tasque/0.1/%{name}-%{version}.tar.gz
License: MIT
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/Tasque
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
