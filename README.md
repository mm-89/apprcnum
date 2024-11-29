# apprcnum

Last update: 29/11/2024

Description of the folder content:

- everything is about the web app:

    apprcnum/
        app.py
        parseRDF.py
        /static/
            example_map.jpg
            styles.css
            LICENSE
        /templates/
            index.html
        
This app is an example of keyword search within the catalog, either by selecting people (thus generating graphs) or by generating the year (producing the object where the word is found).

- everything related to keyword search.

The workflow is as follows: the goal is to search for words "similar" to the patronyms throughout the catalog. Each individual word in the patronyms is selected and then compared to every word in the text within the catalog. The "similarity" is measured in terms of Kolmogorov distance (or alternatively Levenshtein distance) by adjusting the threshold value.

    apprcnum/
        parseWORD.py
        findWORD.py
        kolmogorov.py
        levenshtein.py

parseWORD is a copy of parseRDF, but it is specifically tailored for patronyms and includes preprocessing. findWORD contains the compute_distance function, which extracts words from the text that fall below the threshold.
