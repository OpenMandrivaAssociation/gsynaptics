%define name gsynaptics
%define version 0.9.13
%define release %mkrel 2

Summary: Tool for Synaptics touchpad driver
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://globalbase.dl.sourceforge.jp/gsynaptics/28322/%{name}-%{version}.tar.gz
# non-corrupted icon from CVS
Source1: http://cvs.sourceforge.jp/cgi-bin/viewcvs.cgi/*checkout*/gsynaptics/gsynaptics/data/touchpad.png
License: GPL
Group: System/Configuration/Hardware
Url: http://gsynaptics.sourceforge.jp/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gnomeui2-devel gnome-doc-utils libglade2-devel

%description
GSynaptics is a setting tool for Synaptics touchpad driver.

%prep
%setup -q
cp -f %{SOURCE1} data

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
%update_menus

%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc README TODO
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome/autostart/%{name}-init.desktop
%doc %{_datadir}/gnome/help/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*.1*
%{_datadir}/pixmaps/touchpad.png
