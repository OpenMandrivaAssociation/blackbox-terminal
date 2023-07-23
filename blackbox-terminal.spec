%global optflags %{optflags} -Wno-incompatible-function-pointer-types

Name:           blackbox-terminal
Version:        0.14.0
Release:        1
Summary:        An elegant and customizable terminal for GNOME
License:        GPL-3.0
URL:            https://gitlab.gnome.org/raggesilver/blackbox/
Source0:	https://gitlab.gnome.org/raggesilver/blackbox/-/archive/v%{version}/blackbox-v%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(pqmarble)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  librsvg-vala-devel
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(vapigen)

%description
A beautiful GTK 4 terminal
Black Box is a native terminal emulator for GNOME that offers superb theming options.

With Black Box you can:

Set colors schemes and integrate them with the rest of the window
Customize font and size
Customize keyboard shortcuts
Render Sixel escape sequences
Fully hide the window headerbar
Quickly open links and files by ctrl+clicking file paths and URLs
Easily paste file paths by dragging them into the window
This app is written in Vala and uses GTK 4, libadwaita, and VTE.

%prep
%autosetup -n blackbox-v%{version} -p1

%build
%meson  \
        -Dblackbox_is_flatpak=false
%meson_build

%install
%meson_install

%files 
