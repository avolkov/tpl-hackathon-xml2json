TPL Hackathon
===========

A beginner's attempt at data wrangling.

The goal of this project is to convert all presented XML data into JSON making it more available to the developers.
For further rationale see [presentation_notes.md](documentation/presentation_notes.md) and [TPL_Hackathon_presentation.odp](documentation/TPL_Hackathon_presentation.odp)

The project is written in Python 3.4.3, no external libraries were user, however I used ipdb for debugging.

Source dataset -- http://hackathon.tplcs.ca/data/TPLWebsiteData.2015-11.xml.zip
Converted dataset, 786 MB (11G uncompressed) -- http://data.flamy.ca/tpl.json.xz

If in doubt unpack with http://www.7-zip.org/

# Main scripts

`tpl_xml2json.py` -- reads input `tpl.xml` and outputs `tpl.json`

Run time as measured on a 20GB XML segment, the program running on AMD FX-8329 CPU (3.2GHz) with an HDD

    $ time python tpl_xml2json.py
    real    54m37.292s
    user    51m57.212s
    sys     0m56.504s


`tpl_read_json.py` -- reads in `tpl.json` produced with `tpl_xml2json.py`  and stops at debug point waiting for the user input.

`tpl_count_keys.py` -- count how many times a key with a string value occurs. The application outpus key_stats.json

Runtime as measured on an 11GB json segment, tested on AMD FX-8329 CPU (3.2GHz) with an HDD

    $ time python tpl_count_str_keys.py
    real    4m56.003s
    user    4m51.360s
    sys     0m4.520s

`tpl_count_keys.py` -- uses `key_stats.json` as input, produces `keys_stats_sorted_pretty.json` as output also prints out 10 most frequent and 10 least frequent keys.


Performance

# A sample tpl.xml record:


    <RECORD>
      <PROP NAME="p_record_id">
         <PVAL>EDB0001</PVAL>
      </PROP>
      <PROP NAME="p_title_edb_relevance">
         <PVAL>Academic OneFile</PVAL>
      </PROP>
      <PROP NAME="p_title_edb_relevance">
         <PVAL>Academic One File</PVAL>
      </PROP>
      <PROP NAME="p_title_edb_relevance">
         <PVAL>AcademicOneFile</PVAL>
      </PROP>
      <PROP NAME="p_title_edb_relevance">
         <PVAL>Expanded Academic Index</PVAL>
      </PROP>
      <PROP NAME="p_title_edb_relevance">
         <PVAL>Expanded Academic ASAP</PVAL>
      </PROP>
      <PROP NAME="p_title_edb_relevance">
         <PVAL>Expanded Academic</PVAL>
      </PROP>
      <PROP NAME="p_edb_availability">
         <PVAL>Available anywhere.</PVAL>
      </PROP>
      <PROP NAME="p_item_url">
         <PVAL>http://ezproxy.torontopubliclibrary.ca/login?url=http://infotrac.galegroup.com/itweb/tplmain?db=AONE&amp;id=tplremote1</PVAL>
      </PROP>
      <PROP NAME="p_item_url_inbranch">
         <PVAL>http://infotrac.galegroup.com/itweb/tplmain?db=AONE&amp;id=tplremote1</PVAL>
      </PROP>
      <PROP NAME="p_date_created">
         <PVAL>2009-03-27</PVAL>
      </PROP>
      <PROP NAME="p_date_modified">
         <PVAL>2015-07-22</PVAL>
      </PROP>
      <PROP NAME="p_requires_login">
         <PVAL>Y</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>audiobook review</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>global warming</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>climate change</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>greenhouse gas emissions</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>climate change</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>climatology</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>greenhouse effect</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>desertification</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>ecology</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>book review</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>buyers guide</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>consumers</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>country overview</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>viewpoint essay</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>current controversies</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>history</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>art</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>environment</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>stem cell research</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>genetics</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>animal rights</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>theology</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>medicine</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>literature</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>magazine</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>journal</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>newspaper articles</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>publications</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>periodicals</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>Gay Lesbian Transgendered Issues</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>gardening landscape horticulture</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>Information Science and Library Issues</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>New York Times newspaper</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>arts and humanities</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>biography and genealogy</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>celebrities</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>movie stars</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>musicians and singers</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>business and industries</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>industry</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>company information</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>consumer information</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>government</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>politics</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>political science</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>health and medicine</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>law and law enforcement</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>crime and punishment</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>consumer behavior</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>finance and credit</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>business management</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>sociology</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>science and technology</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>technology and society</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>social sciences</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>society</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>social issues</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>social problems</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>social change</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>social skills</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>corporate social responsibility</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>family policy</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>human development</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>diversity</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>family life</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>drug addiction</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>computers</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>education</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>travel</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>theatre</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>movie reviews</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>film reviews</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>women</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>children</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>men</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>cars and trucks</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>automobiles</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>machines and machinery</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>corporations</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>law</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>earth science</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>astronomy and space</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>authors</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>plants</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>multicultural</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>wildlife habitats</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>cloning</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>alternative medicine</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>energy</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>inventors and inventions</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>maternity and paternity</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>taxation</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>privacy</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>alcohol and tobacco</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>fashion and clothing</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>Canadian constitution</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>natural resources</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>military</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>stock market</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>recession</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>terrorism</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>religion</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>foreign policy</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>developing nations</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>immigration</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>human rights</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>racism and hate crimes</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>wars</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>crime and punishment</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>Darfur</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>Afganistan</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>war in Iraq</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>genocide</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>war crimes</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>Middle East</PVAL>
      </PROP>
      <PROP NAME="p_keywords_edb">
         <PVAL>Rwanda</PVAL>
      </PROP>
      <PROP NAME="p_title_main">
         <PVAL>Academic OneFile</PVAL>
      </PROP>
      <PROP NAME="p_title_sort">
         <PVAL>Academic OneFile</PVAL>
      </PROP>
      <PROP NAME="p_description_en">
         <PVAL>Full-text articles from scholarly, trade and general-interest magazines and journals on current events, general sciences and technology, social sciences, arts and humanities.</PVAL>
      </PROP>
      <PROP NAME="p_branch_id">
         <PVAL>TPL</PVAL>
      </PROP>
      <PROP NAME="p_pub_date_sort">
         <PVAL>2015-07-22</PVAL>
      </PROP>
      <DVAL_ID DIMENSION_ID="20089" ID="20206"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33090"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33091"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33092"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33093"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33094"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33095"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33096"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33097"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33098"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33099"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33100"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33101"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33102"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33103"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33106"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33107"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33108"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33109"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33110"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33111"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33112"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33113"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33114"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33115"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33116"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33117"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33118"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33119"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33120"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33121"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33122"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33123"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33124"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33125"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33126"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33127"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33128"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33129"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33130"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33131"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33132"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33133"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33134"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33135"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33136"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33137"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33138"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33139"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33140"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33141"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33142"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33143"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33144"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33145"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33146"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33147"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33148"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33149"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33150"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33151"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33152"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33153"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33154"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33155"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33156"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33157"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33158"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33159"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33160"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33161"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33162"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33163"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33164"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33165"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33166"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33167"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33168"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33169"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33170"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33171"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33172"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33173"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33174"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33175"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33176"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33177"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33178"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33179"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33180"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33181"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33182"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33183"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33184"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33185"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33186"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33187"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33188"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33189"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33190"/>
      <DVAL_ID DIMENSION_ID="33090" ID="33191"/>
      <DVAL_ID DIMENSION_ID="33090" ID="37801"/>
      <DVAL_ID DIMENSION_ID="27607" ID="37806"/>
      <DVAL_ID DIMENSION_ID="27605" ID="37844"/>
      <DVAL_ID DIMENSION_ID="37864" ID="37939"/>
      <DVAL_ID DIMENSION_ID="37955" ID="38101"/>
      <DVAL_ID DIMENSION_ID="38585" ID="38586"/>
      <DVAL_ID DIMENSION_ID="38589" ID="38596"/>
      <DVAL_ID DIMENSION_ID="33090" ID="38745"/>
      <DVAL_ID DIMENSION_ID="33090" ID="38775"/>
      <DVAL_ID DIMENSION_ID="37749" ID="4289267219"/>
      <DVAL_ID DIMENSION_ID="37749" ID="4289267220"/>
   </RECORD>

A sample output json record:

    {"p_item_url": "http://ezproxy.torontopubliclibrary.ca/login?url=http://infotrac.galegroup.com/itweb/tplmain?db=AONE&id=tplremote1", "dimensions": [{"DIMENSION_ID": 20089, "ID": 20206}, {"DIMENSION_ID": 33090, "ID": 33090}, {"DIMENSION_ID": 33090, "ID": 33091}, {"DIMENSION_ID": 33090, "ID": 33092}, {"DIMENSION_ID": 33090, "ID": 33093}, {"DIMENSION_ID": 33090, "ID": 33094}, {"DIMENSION_ID": 33090, "ID": 33095}, {"DIMENSION_ID": 33090, "ID": 33096}, {"DIMENSION_ID": 33090, "ID": 33097}, {"DIMENSION_ID": 33090, "ID": 33098}, {"DIMENSION_ID": 33090, "ID": 33099}, {"DIMENSION_ID": 33090, "ID": 33100}, {"DIMENSION_ID": 33090, "ID": 33101}, {"DIMENSION_ID": 33090, "ID": 33102}, {"DIMENSION_ID": 33090, "ID": 33103}, {"DIMENSION_ID": 33090, "ID": 33106}, {"DIMENSION_ID": 33090, "ID": 33107}, {"DIMENSION_ID": 33090, "ID": 33108}, {"DIMENSION_ID": 33090, "ID": 33109}, {"DIMENSION_ID": 33090, "ID": 33110}, {"DIMENSION_ID": 33090, "ID": 33111}, {"DIMENSION_ID": 33090, "ID": 33112}, {"DIMENSION_ID": 33090, "ID": 33113}, {"DIMENSION_ID": 33090, "ID": 33114}, {"DIMENSION_ID": 33090, "ID": 33115}, {"DIMENSION_ID": 33090, "ID": 33116}, {"DIMENSION_ID": 33090, "ID": 33117}, {"DIMENSION_ID": 33090, "ID": 33118}, {"DIMENSION_ID": 33090, "ID": 33119}, {"DIMENSION_ID": 33090, "ID": 33120}, {"DIMENSION_ID": 33090, "ID": 33121}, {"DIMENSION_ID": 33090, "ID": 33122}, {"DIMENSION_ID": 33090, "ID": 33123}, {"DIMENSION_ID": 33090, "ID": 33124}, {"DIMENSION_ID": 33090, "ID": 33125}, {"DIMENSION_ID": 33090, "ID": 33126}, {"DIMENSION_ID": 33090, "ID": 33127}, {"DIMENSION_ID": 33090, "ID": 33128}, {"DIMENSION_ID": 33090, "ID": 33129}, {"DIMENSION_ID": 33090, "ID": 33130}, {"DIMENSION_ID": 33090, "ID": 33131}, {"DIMENSION_ID": 33090, "ID": 33132}, {"DIMENSION_ID": 33090, "ID": 33133}, {"DIMENSION_ID": 33090, "ID": 33134}, {"DIMENSION_ID": 33090, "ID": 33135}, {"DIMENSION_ID": 33090, "ID": 33136}, {"DIMENSION_ID": 33090, "ID": 33137}, {"DIMENSION_ID": 33090, "ID": 33138}, {"DIMENSION_ID": 33090, "ID": 33139}, {"DIMENSION_ID": 33090, "ID": 33140}, {"DIMENSION_ID": 33090, "ID": 33141}, {"DIMENSION_ID": 33090, "ID": 33142}, {"DIMENSION_ID": 33090, "ID": 33143}, {"DIMENSION_ID": 33090, "ID": 33144}, {"DIMENSION_ID": 33090, "ID": 33145}, {"DIMENSION_ID": 33090, "ID": 33146}, {"DIMENSION_ID": 33090, "ID": 33147}, {"DIMENSION_ID": 33090, "ID": 33148}, {"DIMENSION_ID": 33090, "ID": 33149}, {"DIMENSION_ID": 33090, "ID": 33150}, {"DIMENSION_ID": 33090, "ID": 33151}, {"DIMENSION_ID": 33090, "ID": 33152}, {"DIMENSION_ID": 33090, "ID": 33153}, {"DIMENSION_ID": 33090, "ID": 33154}, {"DIMENSION_ID": 33090, "ID": 33155}, {"DIMENSION_ID": 33090, "ID": 33156}, {"DIMENSION_ID": 33090, "ID": 33157}, {"DIMENSION_ID": 33090, "ID": 33158}, {"DIMENSION_ID": 33090, "ID": 33159}, {"DIMENSION_ID": 33090, "ID": 33160}, {"DIMENSION_ID": 33090, "ID": 33161}, {"DIMENSION_ID": 33090, "ID": 33162}, {"DIMENSION_ID": 33090, "ID": 33163}, {"DIMENSION_ID": 33090, "ID": 33164}, {"DIMENSION_ID": 33090, "ID": 33165}, {"DIMENSION_ID": 33090, "ID": 33166}, {"DIMENSION_ID": 33090, "ID": 33167}, {"DIMENSION_ID": 33090, "ID": 33168}, {"DIMENSION_ID": 33090, "ID": 33169}, {"DIMENSION_ID": 33090, "ID": 33170}, {"DIMENSION_ID": 33090, "ID": 33171}, {"DIMENSION_ID": 33090, "ID": 33172}, {"DIMENSION_ID": 33090, "ID": 33173}, {"DIMENSION_ID": 33090, "ID": 33174}, {"DIMENSION_ID": 33090, "ID": 33175}, {"DIMENSION_ID": 33090, "ID": 33176}, {"DIMENSION_ID": 33090, "ID": 33177}, {"DIMENSION_ID": 33090, "ID": 33178}, {"DIMENSION_ID": 33090, "ID": 33179}, {"DIMENSION_ID": 33090, "ID": 33180}, {"DIMENSION_ID": 33090, "ID": 33181}, {"DIMENSION_ID": 33090, "ID": 33182}, {"DIMENSION_ID": 33090, "ID": 33183}, {"DIMENSION_ID": 33090, "ID": 33184}, {"DIMENSION_ID": 33090, "ID": 33185}, {"DIMENSION_ID": 33090, "ID": 33186}, {"DIMENSION_ID": 33090, "ID": 33187}, {"DIMENSION_ID": 33090, "ID": 33188}, {"DIMENSION_ID": 33090, "ID": 33189}, {"DIMENSION_ID": 33090, "ID": 33190}, {"DIMENSION_ID": 33090, "ID": 33191}, {"DIMENSION_ID": 33090, "ID": 37801}, {"DIMENSION_ID": 27607, "ID": 37806}, {"DIMENSION_ID": 27605, "ID": 37844}, {"DIMENSION_ID": 37864, "ID": 37939}, {"DIMENSION_ID": 37955, "ID": 38101}, {"DIMENSION_ID": 38585, "ID": 38586}, {"DIMENSION_ID": 38589, "ID": 38596}, {"DIMENSION_ID": 33090, "ID": 38745}, {"DIMENSION_ID": 33090, "ID": 38775}, {"DIMENSION_ID": 37749, "ID": 4289267219}, {"DIMENSION_ID": 37749, "ID": 4289267220}], "p_edb_availability": "Available anywhere.", "p_requires_login": "Y", "p_record_id": "EDB0001", "p_item_url_inbranch": "http://infotrac.galegroup.com/itweb/tplmain?db=AONE&id=tplremote1", "p_date_modified": "2015-07-22", "p_description_en": "Full-text articles from scholarly, trade and general-interest magazines and journals on current events, general sciences and technology, social sciences, arts and humanities.", "p_title_main": "Academic OneFile", "p_date_created": "2009-03-27", "p_title_edb_relevance": ["Academic OneFile", "Academic One File", "AcademicOneFile", "Expanded Academic Index", "Expanded Academic ASAP", "Expanded Academic"], "p_branch_id": "TPL", "p_keywords_edb": ["audiobook review", "global warming", "climate change", "greenhouse gas emissions", "climatology", "greenhouse effect", "desertification", "ecology", "book review", "buyers guide", "consumers", "country overview", "viewpoint essay", "current controversies", "history", "art", "environment", "stem cell research", "genetics", "animal rights", "theology", "medicine", "literature", "magazine", "journal", "newspaper articles", "publications", "periodicals", "Gay Lesbian Transgendered Issues", "gardening landscape horticulture", "Information Science and Library Issues", "New York Times newspaper", "arts and humanities", "biography and genealogy", "celebrities", "movie stars", "musicians and singers", "business and industries", "industry", "company information", "consumer information", "government", "politics", "political science", "health and medicine", "law and law enforcement", "crime and punishment", "consumer behavior", "finance and credit", "business management", "sociology", "science and technology", "technology and society", "social sciences", "society", "social issues", "social problems", "social change", "social skills", "corporate social responsibility", "family policy", "human development", "diversity", "family life", "drug addiction", "computers", "education", "travel", "theatre", "movie reviews", "film reviews", "women", "children", "men", "cars and trucks", "automobiles", "machines and machinery", "corporations", "law", "earth science", "astronomy and space", "authors", "plants", "multicultural", "wildlife habitats", "cloning", "alternative medicine", "energy", "inventors and inventions", "maternity and paternity", "taxation", "privacy", "alcohol and tobacco", "fashion and clothing", "Canadian constitution", "natural resources", "military", "stock market", "recession", "terrorism", "religion", "foreign policy", "developing nations", "immigration", "human rights", "racism and hate crimes", "wars", "Darfur", "Afganistan", "war in Iraq", "genocide", "war crimes", "Middle East", "Rwanda"], "p_pub_date_sort": "2015-07-22", "p_title_sort": "Academic OneFile"}
