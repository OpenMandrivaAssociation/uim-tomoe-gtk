%define name	uim-tomoe-gtk
%define version	0.5.0
%define release	%mkrel 1

Name:		uim-tomoe-gtk
Summary:	A tool for providing tomoe support to uim
Version:	%{version}
Release:	%{release}
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
BuildRequires:          libm17n-lib
BuildRequires:	 	libtomoe-gtk-devel

%description
A tool for providing tomoe support to uim.

%prep
%setup -q

%build
%configure
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


