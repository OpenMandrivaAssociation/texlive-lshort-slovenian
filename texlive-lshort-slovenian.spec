# revision 15878
# category Package
# catalog-ctan /info/lshort/slovenian
# catalog-date 2008-08-22 10:50:40 +0200
# catalog-license gpl
# catalog-version 4.20
Name:		texlive-lshort-slovenian
Version:	4.20
Release:	7
Summary:	Slovenian translation of lshort
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/slovenian
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-slovenian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-slovenian.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A Slovenian translation of the Not So Short Introduction to
LaTeX 2e.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/README
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/lshort-slovenian.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/biblio.tex
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/contrib.tex
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/custom.tex
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/fancyhea.sty
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/graphic.tex
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/lshort-a5.tex
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/lshort-base.tex
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/lshort-slovenian.sty
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/lshort-slovenian.tex
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/lssym.tex
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/math.tex
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/mylayout.sty
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/overview.tex
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/spec.tex
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/things.tex
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/title.tex
%doc %{_texmfdistdir}/doc/latex/lshort-slovenian/src/typeset.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.20-2
+ Revision: 753482
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.20-1
+ Revision: 718902
- texlive-lshort-slovenian
- texlive-lshort-slovenian
- texlive-lshort-slovenian
- texlive-lshort-slovenian

