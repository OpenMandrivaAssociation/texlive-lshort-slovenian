Name:		texlive-lshort-slovenian
Version:	68204
Release:	1
Summary:	Slovenian translation of lshort
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/slovenian
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-slovenian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-slovenian.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
