#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	XML::Sablotron perl module
Summary(pl.UTF-8):	Moduł perla XML::Sablotron
Name:		perl-XML-Sablotron
Version:	1.01
Release:	1
License:	GPL v2+ or MPL v1.1
Group:		Development/Languages/Perl
#Source0Download:	http://www.gingerall.com/charlie/ga/xml/d_sab.xml
Source0:	http://download-1.gingerall.cz/download/sablot/XML-Sablotron-%{version}.tar.gz
# Source0-md5:	d9d21b20bff8b04c966b9c3b678989c1
# incomplete, see comments inside if you want to finish
Patch0:		%{name}-types.patch
URL:		http://www.gingerall.com/charlie/ga/xml/p_sab.xml
BuildRequires:	expat-devel > 1.95
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	sablotron-devel
# see unfinished patch0
ExcludeArch:	%{x8664} alpha ia64 ppc64 sparc64 s390x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Sablotron is a simple Perl package, which encapsulates the C API
of Sablotron XSLT processor.

%description -l pl.UTF-8
XML::Sablotron to prosty pakiet Perla zawierający interfejs do API
procesora XSLT Sablotron.

%prep
%setup -q -n XML-Sablotron-%{version}
#%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorarch}/XML/Sablotron.pm
%{perl_vendorarch}/XML/Sablotron
%dir %{perl_vendorarch}/auto/XML/Sablotron
%{perl_vendorarch}/auto/XML/Sablotron/Sablotron.bs
%attr(755,root,root) %{perl_vendorarch}/auto/XML/Sablotron/Sablotron.so
%{_mandir}/man3/*
