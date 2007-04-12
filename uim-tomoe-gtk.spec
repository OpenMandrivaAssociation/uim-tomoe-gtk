%define version	0.2.0
%define release	%mkrel 2

%define libtomoe-gtk_version 0.1.0

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
Requires:		libtomoe-gtk >= %{libtomoe-gtk_version}
BuildRequires:		gtk+2-devel >= 2.8.0
BuildRequires:		libuim-devel
BuildRequires:		libtomoe-devel >= %{tomoe_version}
BuildRequires:          automake1.8 
BuildRequires:          tomoe
BuildRequires:          libm17n-lib
BuildRequires:	 libtomoe-gtk-devel

%description
A tool for providing tomoe support to uim.


%prep
%setup -q
cp /usr/share/automake-1.9/mkinstalldirs .

%build
[[ ! -x configure ]] && ./autogen.sh
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


