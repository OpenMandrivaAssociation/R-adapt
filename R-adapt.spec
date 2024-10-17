%global packname  adapt
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0_4
Release:          3
Summary:          adapt -- multidimensional numerical integration
Group:            Sciences/Mathematics
License:          Unclear (Fortran) -- code in Statlib's ./S/adapt
URL:              https://cran.r-project.org/web/packages/adapt/index.html
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


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0_4-1
+ Revision: 774811
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-7mdv2011.0
+ Revision: 616445
- the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.0.4-6mdv2010.0
+ Revision: 433070
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-5mdv2009.0
+ Revision: 260120
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-4mdv2009.0
+ Revision: 248095
- rebuild

* Fri Feb 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.4-2mdv2008.1
+ Revision: 176960
- remove requires on libR.so

* Sun Feb 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.4-1mdv2008.1
+ Revision: 169982
- complete spec file
- fix Url
- add source and spec file
- Created package structure for R-cran-adapt.

