from StringIO import StringIO
from Bio import Entrez, Medline

def search_medline(query, email):
    Entrez.email = email
    search = Entrez.esearch(db='pubmed', term=query, usehistory='y')
    handle = Entrez.read(search)
    try:
        return handle
    except Exception as e:
        raise IOError(str(e))
    finally:
        search.close()

def fetch_rec(rec_id, entrez_handle):
    fetch_handle = Entrez.efetch(db='pubmed', id=rec_id,
                                 rettype='Medline', retmode='text',
                                 webenv=entrez_handle['WebEnv'],
                                 query_key=entrez_handle['QueryKey'])
    rec = fetch_handle.read()
    return rec

def main(query, email):
    rec_handler = search_medline(query, email)

    for rec_id in rec_handler['IdList']:
        rec = fetch_rec(rec_id, rec_handler)
        rec_file = StringIO(rec)
        medline_rec = Medline.read(rec_file)
        if 'AB' in medline_rec:
            print(medline_rec['AB'])

if __name__ == '__main__':
    email = "deep.dhungel@fu-berlin.de"
    query = "diabetes AND schizophrenia"
    main(query, email)