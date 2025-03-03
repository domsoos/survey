# Repository for Automatic Science News Detection, Evaluation, and Generation: A Survey


## Google Scholar Scraper

The following queries were used to obtain the top 100 results by Google Scholar in each Science News detection, evaluation and generation.

**Detection**   
```bash
python3 scholar_scraper.py 'intitle:"science news"OR"scientific news" automatic AND detection' detection.csv
```

**Evaluation**  
```bash
python3 scholar_scraper.py 'intitle:"science news"OR"scientific news" automatic AND evaluation' evaluation.csv
```

**Generation**  
```bash
python3 scholar_scraper.py 'intitle:"science news"OR"scientific news" automatic AND generation' generation.csv 
```

