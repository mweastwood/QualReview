review.pdf: *.tex aas_macros.sty
	pdflatex review.tex
	pdflatex review.tex
clean:
	rm *.aux *.log *.toc *.out review.pdf
