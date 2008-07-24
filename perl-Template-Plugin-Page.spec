%define realname Template-Plugin-Page
%define name perl-%realname
%define version 0.10
%define release %mkrel 5

Summary:	A plugin to help when paging through sets of results
Name:		%name
Version:	%version
Release:	%release
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%realname/
Source:		%realname-%version.tar.bz2
BuildRequires:	perl-devel perl-Data-Page
BuildRequires:  perl-Template-Toolkit
BuildArch:	noarch
Buildroot:	%_tmppath/%name-root

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
%setup -q -n %realname-%version

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{make}

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%perl_vendorlib/Template/Plugin/*
%_mandir/*/*

%clean
rm -rf $RPM_BUILD_ROOT

