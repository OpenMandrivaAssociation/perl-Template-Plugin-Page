%define upstream_name    Template-Plugin-Page
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A plugin to help when paging through sets of results
License:	Artistic/GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Data::Page)
BuildRequires:  perl(Template)
BuildArch:	noarch

%description
When searching through large amounts of data, it is often the case
that a result set is returned that is larger than we want to display
on one page. This results in wanting to page through various pages of
data. The maths behind this is unfortunately fiddly, hence this
module.

The main concept is that you pass in the number of total entries, the
number of entries per page, and the current page number. You can then
call methods to find out how many pages of information there are, and
what number the first and last entries on the current page really are.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Template/Plugin/*
%{_mandir}/*/*

%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 408083
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.10-6mdv2009.0
+ Revision: 258476
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.10-5mdv2009.0
+ Revision: 246507
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.10-3mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-3mdv2008.0
+ Revision: 86943
- rebuild


* Mon Jan 16 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.10-2mdk
- Add BuildRequires: perl-Template-Toolkit

* Sun Jan 15 2006 Frederic Lepied <flepied@mandriva.com> 0.10-1mdk
- Initial package

