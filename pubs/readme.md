Cómo usarlo

1. Instala las dependencias

Abre tu terminal y ejecuta:

* pip install bibtexparser
  

1. Exporta tus publicaciones desde Google Scholar o WOS como .bib
En Google Scholar: haz clic en “Cite” → selecciona “BibTeX” → copia y pega en un archivo publications.bib
En Web of Science: exporta como “EndNote → File” → luego conviértelo a .bib con Zotero o BibTeX Converter

1. Guarda el script como bibtex_to_yaml.py en la raíz de tu sitio Jekyll
1. Ejecuta el script

* python bibtex_to_yml.py
  
1. ¡Listo!
Se generará _data/publications.yml


## TODO

**verificar que todos los bib tienen el año puesto**
