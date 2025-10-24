---
title: "Research Group"
layout: single
author_profile: true
permalink: /group/
---

<div id="toc"></div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const toc = document.getElementById('toc');
    const headers = Array.from(document.querySelectorAll('h2, h3'));
    let tocHTML = '<h3>Table of Contents</h3><ul>';
    
    headers.forEach(header => {
      const id = header.id || header.textContent.toLowerCase().replace(/[^\w]+/g, '-').replace(/^-+|-+$/g, '');
      header.id = id; // Asegura que cada sección tenga un ID
      const text = header.textContent.trim();
      const level = header.tagName === 'H2' ? 1 : 2;
      const indent = '  '.repeat(level - 1);
      tocHTML += `<li style="margin-left: ${level * 15}px;"><a href="#${id}">${text}</a></li>`;
    });
    
    tocHTML += '</ul>';
    toc.innerHTML = tocHTML;
  });
</script>

## Senior Researchers

### All Senior Researchers
- [Dr. Luca Martino](#luca-martino)
- [Dr. Oscar Barquero](#oscar-barquero)
- [Dr. Ana López](#ana-lopez)
- [Dr. Miguel Ruiz](#miguel-ruiz)

---

### Dr. Luca Martino {#luca-martino}
<div style="width: 160px; height: 160px; border-radius: 50%; background-image: url('/assets/images/luca.jpg'); background-size: contain; background-position: center; background-repeat: no-repeat; border: 2px solid #f0f0f0; box-shadow: 0 1px 4px rgba(0,0,0,0.1); margin: 0 1rem 1rem 0; display: inline-block; vertical-align: top;"></div>
**Dr. Luca Martino** is a Senior Researcher in statistical modeling for medical data. His work focuses on Bayesian inference, survival analysis, and the development of robust methods for hazard ratio estimation. He has co-authored over 40 peer-reviewed publications and leads the group’s methodological core.

[🔗 Google Scholar](https://scholar.google.com/citations?user=XXXX) | [📧 Email](mailto:luca.martino@university.edu)

---

### Dr. Oscar Barquero {#oscar-barquero}
<div style="width: 160px; height: 160px; border-radius: 50%; background-image: url('/assets/images/oscar.jpg'); background-size: contain; background-position: center; background-repeat: no-repeat; border: 2px solid #f0f0f0; box-shadow: 0 1px 4px rgba(0,0,0,0.1); margin: 0 1rem 1rem 0; display: inline-block; vertical-align: top;"></div>
**Dr. Oscar Barquero** specializes in computational epidemiology and social determinants of health. His recent work analyzes health disparities using longitudinal cohort data and machine learning. He collaborates closely with public health agencies and is a co-founder of the group’s open-data initiative.

[🔗 GitHub](https://github.com/oscarbarquero) | [📧 Email](mailto:oscar.barquero@university.edu)

---

### Dr. Ana López {#ana-lopez}
<div style="width: 160px; height: 160px; border-radius: 50%; background-image: url('/assets/images/ana.jpg'); background-size: contain; background-position: center; background-repeat: no-repeat; border: 2px solid #f0f0f0; box-shadow: 0 1px 4px rgba(0,0,0,0.1); margin: 0 1rem 1rem 0; display: inline-block; vertical-align: top;"></div>
**Dr. Ana López** is an expert in causal inference and health policy evaluation. Her research combines quasi-experimental designs with administrative data to assess the impact of social interventions. She teaches advanced biostatistics at the graduate level.

[📧 Email](mailto:ana.lopez@university.edu)

---

### Dr. Miguel Ruiz {#miguel-ruiz}
<div style="width: 160px; height: 160px; border-radius: 50%; background-image: url('/assets/images/miguel.jpg'); background-size: contain; background-position: center; background-repeat: no-repeat; border: 2px solid #f0f0f0; box-shadow: 0 1px 4px rgba(0,0,0,0.1); margin: 0 1rem 1rem 0; display: inline-block; vertical-align: top;"></div>
**Dr. Miguel Ruiz** develops statistical software for reproducible research. He maintains the group’s R/Python pipelines and leads training workshops on open science practices. His work has been adopted by several international research consortia.

[🔗 GitHub](https://github.com/miguelruiz) | [📧 Email](mailto:miguel.ruiz@university.edu)

---

## PhD Students

### All PhD Students
- [Isabel García](#isabel-garcia)
- [Diego Fernández](#diego-fernandez)
- [Sofía Morales](#sofia-morales)
- [Tomás Ruiz](#tomás-ruiz)

---

### Isabel García {#isabel-garcia}
<div style="width: 160px; height: 160px; border-radius: 50%; background-image: url('/assets/images/isabel.jpg'); background-size: contain; background-position: center; background-repeat: no-repeat; border: 2px solid #f0f0f0; box-shadow: 0 1px 4px rgba(0,0,0,0.1); margin: 0 1rem 1rem 0; display: inline-block; vertical-align: top;"></div>
**Isabel García** is investigating the use of machine learning to predict treatment response in chronic pain patients using electronic health records. Her work is funded by the National Health Institute.

[🔗 GitHub](https://github.com/isabelgarcia) | [📧 Email](mailto:isabel.garcia@university.edu)

---

### Diego Fernández {#diego-fernandez}
<div style="width: 160px; height: 160px; border-radius: 50%; background-image: url('/assets/images/diego.jpg'); background-size: contain; background-position: center; background-repeat: no-repeat; border: 2px solid #f0f0f0; box-shadow: 0 1px 4px rgba(0,0,0,0.1); margin: 0 1rem 1rem 0; display: inline-block; vertical-align: top;"></div>
**Diego Fernández** studies social determinants of mental health disparities in urban populations. He combines geospatial analysis with survey data to identify neighborhood-level risk factors.

[📧 Email](mailto:diego.fernandez@university.edu)

---

### Sofía Morales {#sofia-morales}
<div style="width: 160px; height: 160px; border-radius: 50%; background-image: url('/assets/images/sofia.jpg'); background-size: contain; background-position: center; background-repeat: no-repeat; border: 2px solid #f0f0f0; box-shadow: 0 1px 4px rgba(0,0,0,0.1); margin: 0 1rem 1rem 0; display: inline-block; vertical-align: top;"></div>
**Sofía Morales** works on causal mediation analysis in longitudinal studies of aging. She develops new R packages for robust estimation of indirect effects under missing data.

[🔗 GitHub](https://github.com/sofiamorales) | [📧 Email](mailto:sofia.morales@university.edu)

---

### Tomás Ruiz {#tomás-ruiz}
<div style="width: 160px; height: 160px; border-radius: 50%; background-image: url('/assets/images/tomas.jpg'); background-size: contain; background-position: center; background-repeat: no-repeat; border: 2px solid #f0f0f0; box-shadow: 0 1px 4px rgba(0,0,0,0.1); margin: 0 1rem 1rem 0; display: inline-block; vertical-align: top;"></div>
**Tomás Ruiz** explores the intersection of health economics and behavioral science. His current project evaluates the impact of financial incentives on medication adherence in low-income populations.

[📧 Email](mailto:tomas.ruiz@university.edu)

---

## Former PhD Students

### Alumni
- [Dr. Carla Jiménez](#carla-jimenez) — Postdoc, Stanford University
- [Dr. Roberto Díaz](#roberto-diaz) — Data Scientist, Google Health
- [Dr. Elena Vargas](#elena-vargas) — Research Lead, WHO Regional Office

---

### Dr. Carla Jiménez {#carla-jimenez}
<div style="width: 160px; height: 160px; border-radius: 50%; background-image: url('/assets/images/carla.jpg'); background-size: contain; background-position: center; background-repeat: no-repeat; border: 2px solid #f0f0f0; box-shadow: 0 1px 4px rgba(0,0,0,0.1); margin: 0 1rem 1rem 0; display: inline-block; vertical-align: top;"></div>
**Dr. Carla Jiménez** completed her PhD in 2022. She now leads a team at Stanford developing AI tools for early detection of sepsis. Her thesis on dynamic hazard models received the Best Dissertation Award.

[🔗 LinkedIn](https://linkedin.com/in/carla-jimenez) | [📧 Email](mailto:carla.jimenez@stanford.edu)

---

### Dr. Roberto Díaz {#roberto-diaz}
<div style="width: 160px; height: 160px; border-radius: 50%; background-image: url('/assets/images/roberto.jpg'); background-size: contain; background-position: center; background-repeat: no-repeat; border: 2px solid #f0f0f0; box-shadow: 0 1px 4px rgba(0,0,0,0.1); margin: 0 1rem 1rem 0; display: inline-block; vertical-align: top;"></div>
**Dr. Roberto Díaz** graduated in 2021 and joined Google Health as a Data Scientist. He applies statistical learning to clinical decision support systems. He remains a frequent collaborator with the group.

[🔗 GitHub](https://github.com/robertodiaz) | [📧 Email](mailto:roberto.diaz@google.com)

---

### Dr. Elena Vargas {#elena-vargas}
<div style="width: 160px; height: 160px; border-radius: 50%; background-image: url('/assets/images/elena.jpg'); background-size: contain; background-position: center; background-repeat: no-repeat; border: 2px solid #f0f0f0; box-shadow: 0 1px 4px rgba(0,0,0,0.1); margin: 0 1rem 1rem 0; display: inline-block; vertical-align: top;"></div>
**Dr. Elena Vargas** completed her PhD in 2020 and now leads the Health Equity Unit at WHO. Her work focuses on global access to diagnostics and statistical capacity building in low-resource settings.

[🔗 WHO Profile](https://www.who.int/staff/elena-vargas) | [📧 Email](mailto:elena.vargas@who.int)
