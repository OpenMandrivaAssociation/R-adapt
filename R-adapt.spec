%global packname  adapt
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0_4
Release:          1
Summary:          adapt -- multidimensional numerical integration
Group:            Sciences/Mathematics
License:          Unclear (Fortran) -- code in Statlib's ./S/adapt
URL:              http://cran.r-project.org/web/packages/adapt/index.html
Source0:          http://cran.r-project.org/src/contrib/Archive/adapt/adapt_1.0-4.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
%rename R-cran-adapt

%description
Adaptive Quadrature in up to 20 dimensions
%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
