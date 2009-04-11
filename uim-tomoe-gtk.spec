%define name	uim-tomoe-gtk
%define version	0.6.0

Name:		uim-tomoe-gtk
Summary:	A tool for providing tomoe support to uim
Version:	%{version}
Release:	%mkrel 3
Group:		System/Internationalization
License:	LGPL
URL:  		https://sourceforge.jp/projects/tomoe/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		uim tomoe
BuildRequires:		gtk+2-devel
BuildRequires:		libuim-devel
BuildRequires:		libtomoe-devel
BuildRequires:          tomoe
BuildRequires:          m17n-lib-devel
BuildRequires:	 	libtomoe-gtk-devel

%description
A tool for providing tomoe support to uim.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_bindir}/*
