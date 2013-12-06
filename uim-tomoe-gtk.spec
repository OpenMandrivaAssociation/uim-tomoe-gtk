Summary:	A tool for providing tomoe support to uim
Name:		uim-tomoe-gtk
Version:	0.6.0
Release:	13
Group:		System/Internationalization
License:	LGPLv2
Url:		https://sourceforge.jp/projects/tomoe/
Source0:	%{name}-%{version}.tar.bz2
BuildREquires:	intltool
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(m17n-core)
BuildRequires:	pkgconfig(tomoe)
BuildRequires:	pkgconfig(tomoe-gtk)
BuildRequires:	pkgconfig(uim)
Requires:	tomoe
Requires:	uim

%description
A tool for providing tomoe support to uim.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog
%{_bindir}/*

