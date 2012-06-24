#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	XML::Sablotron perl module
Summary(pl):	Modu� perla XML::Sablotron
Name:		perl-XML-Sablotron
Version:	1.0
Release:	1
License:	GPL v2+ or MPL v1.1
Group:		Development/Languages/Perl
Source0:	http://download-2.gingerall.cz/download/sablot/XML-Sablotron-%{version}.tar.gz
# Source0-md5:	f9825c7f9a2243841de65bba9310fa58
BuildRequires:	expat-devel > 1.95
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sablotron-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Sablotron is a simple Perl package, which encapsulates the C API
of Sablotron XSLT processor.

%description -l pl
XML::Sablotron to prosty pakiet Perla zawieraj�cy interfejs do API
procesora XSLT Sablotron.

%prep
%setup -q -n XML-Sablotron-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
