# Solutions

L'enonce de l'exercice est disponible [ici](./enonce.md)

## Installation :

- Avec `brew` : 

```
$ brew install siege
```

- Avec `apt` ou `apt-get`:

```
$ apt install siege
```

- Autre :

```
$ wget http://download.joedog.org/siege/siege-3.1.4.tar.gz

$ tar -zxvf siege-3.1.4.tar.gz

$ cd siege-*/

$ ./configure --prefix=/some/dir --with-ssl=/usr/local/ssl

$ make uninstall ( si vous l'avez déjà installé)

$ make install

```

## Documentation 

```
Read the documentation
   The online help is pretty straight forward ( siege --help ):
   Usage: siege [options]
   Options:
    -V, --version        VERSION, prints version number to screen.
    -h, --help           HELP, prints this section.
    -v, --verbose        VERBOSE, prints notification to screen.
    -c, --concurrent=NUM CONCURRENT users, default is 10
    -u, --url="URL"      URL, a single user defined URL for stress testing.
    -i, --internet       INTERNET user simulation, hits the URLs randomly.
    -b, --benchmark      BENCHMARK, signifies no delay for time testing.
    -t, --times=NUM      TIMES, number of times to run the test, default is 25
    -t, --time=NUMm      TIME based testing where "m" is the modifier S, M, or H
                         no space between NUM and "m", ex: --time=1H, 1 hour test.
    -f, --file=FILE      FILE, change the configuration file to file.
    -l, --log            LOG, logs the transaction to PREFIX/var/siege.log
    -m, --mark="text"    MARK, mark the log file with a string separator.
    -d, --delay=NUM      Time DELAY, random delay between 1 and num designed
                         to simulate human activity. Default value is 3  

   For more detailed information, consult the man pages:
   $ man siege
   $ man layingsiege
   $ man siege.config

   All the siege man pages are also available online:
   http://www.joedog.org/siege/docs/man/index.html

   OR, read the html manual, doc/manual.html  The manual is also available online:
   http://www.joedog.org/siege/docs/manual.html 

```

## Correction

- Les tests ont été faits sur l'atelier [AJAX](../Ajax)

1. `siege http://127.0.0.1:5000/ -t1m`

2. `siege -f ./urls.txt -t5m`

3. La valeur `concurrency` représente la capacité maximale de connexions simultanées.

4. `siege -f ./urls.txt -c3 -t30m`