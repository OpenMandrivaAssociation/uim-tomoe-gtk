%define name	uim-tomoe-gtk
%define version	0.6.0

Name:		uim-tomoe-gtk
Summary:	A tool for providing tomoe support to uim
Version:	%{version}
Release:	%mkrel 8
Group:		System/Internationalization
License:	LGPL
URL:  		https://sourceforge.jp/projects/tomoe/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		uim tomoe
BuildRequires:		gtk+2-devel
BuildRequires:		uim-devel
BuildRequires:		tomoe-devel
BuildRequires:          tomoe
BuildRequires:          m17n-lib-devel
BuildRequires:	 	tomoe-gtk-devel
BuildREquires:		intltool

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


%changelog
* Mon May 09 2011 Funda Wang <fwang@mandriva.org> 0.6.0-6mdv2011.0
+ Revision: 672718
- br intltool

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-5mdv2011.0
+ Revision: 524301
- rebuilt for 2010.1

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 0.6.0-4mdv2009.1
+ Revision: 366395
- bump rel
- fix BR
- fix BR

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.6.0-3mdv2009.0
+ Revision: 225897
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-2mdv2008.1
+ Revision: 179669
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Funda Wang <fwang@mandriva.org> 0.6.0-1mdv2008.0
+ Revision: 46271
- New version

* Sat Jun 16 2007 Adam Williamson <awilliamson@mandriva.org> 0.5.0-1mdv2008.0
+ Revision: 40213
- clean spec; trim buildrequires; new release 0.5.0; rebuild for new era


* Fri Nov 18 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.2.0-2mdk
- rebuild against openssl-0.9.8

* Sat Oct 29 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.2.0-1mdk
- new release
- add requires libtomoe-gtk

* Wed Aug 24 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.1.1-3mdk
- rebuild with new gtk+

* Sun Jul 31 2005 Nicolas L�ureuil <neoclust@mandriva.org> 0.1.1-2mdk
- Fix BuildRequires

* Thu Feb 17 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.1.1-1mdk
- first spec for Mandrakelinux

