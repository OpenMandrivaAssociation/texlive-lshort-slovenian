%global tl_name lshort-slovenian
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.20
Release:	%{tl_revision}.1
Summary:	Slovenian translation of lshort
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/slovenian
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-slovenian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-slovenian.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A Slovenian translation of the Not So Short Introduction to LaTeX2e.

