Sphinx per la tesi di laurea al DI
==================================

![CC SA3.0](http://i.creativecommons.org/l/by-sa/3.0/88x31.png)

Questo repository contiene un esempio di utilizzo di [Sphinx](http://sphinx-doc.org/) come strumento di supporto per la stesura della tesi; il suo contenuto
è distribuito sotto licenza [Creative Commons Attribution-ShareAlike 3.0 Unported
License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US>).

Per utilizzare questo materiale è necessario installare alcuni pacchetti
Python, la cosa più comoda per farlo è installare
[virutlaenv](https://virtualenv.pypa.io/en/latest/) e quindi dare i comandi

	virtualenv sw
  	. ./sw/bin/activate
  	pip install -r requirements.txt

Una volta installate le dipendenze, si può procedere alla compilazione delle
versioni HTML e PDF rispettivamente con

	make html
	make pdf

che genereranno (in assenza di errori) il risultato della compilazione
rispettivamente nei file

	build/html/index.html
	build/pdf/Tesi.pdf

[![Analytics](https://ga-beacon.appspot.com/UA-49277456-5/sphinx4tesi?pixel)](https://github.com/igrigorik/ga-beacon)
