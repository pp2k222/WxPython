import pdfkit
import datetime
import os

def generate_Umowa_PDF(oferta , path):
    index = 1
    cenaZL1 = 0
    cenaZL2 = 0
    wartosc_brutto = 0
    table = """ <!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">

    <style>


        .keep-together {
            margin-top:20px;
    page-break-inside: avoid;
}


        td {
            padding: 0;
            margin: 0;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            font-size: 14px;
        }
        .property_container {
            margin-left: 20%;
            width: 75%;
            margin-right: 5%;
        }
        .property_container{
            text-align:center;
        }

        .value9 tr td{
            text-align:center;
            white-space: normal !important;
            word-wrap: break-word;
        }
        .property , .property_dodatki, .value9 {
            border-collapse: collapse;

            width: 100%;
        }
        .property_dodatki, .value9{
            margin-top:5px;
            margin-bottom:10px;

        }
        .property td , .property_dodatki td  {
            border-top: solid 1px #91CAD8;
            padding:2px;

        }

        .property td:nth-child(odd) {
            text-align: right;
            font-weight: bold;
            max-width: 25%;
            white-space: normal !important;
            word-wrap: break-word;
            min-width:200px;
            max-width: 250px;
        }

        .property td:nth-child(even) {
            text-align: left;
            padding-left: 5px;
            width:100%;
            white-space: normal !important;
            word-wrap: break-word;
        }

        .property tr:nth-child(even) , .property_dodatki tr:nth-child(even)  {
            background: #e8faff;
        }

        .header {
            border-collapse: collapse;
            width: 90%;
            text-align: center;
            margin: auto;
        }
        .text{

            width:90%;
            margin:auto;
            margin-top:50px;
        }
        .header  th {
            border-bottom: solid 1px #91CAD8;
            width: 15%;
        }

        .header th:nth-child(1) {
            border-bottom: solid 4px #91CAD8;


        }
        .propertyHeader{
            border-bottom: solid 1px #91CAD8;
            padding-top:5px;
            font-size:24px;
            width:13%;
            font-weight:bold;
            margin-left:7%;
            margin-bottom:-1px;
        }

        .header td {
            border-bottom: solid 4px #91CAD8;

        }

        .PosNumber {
            width: 25%;

            font-size: 20px;
            background-color: #c7c7c7;
        }
    </style>
    <title>Page Title</title>
</head>

<body>""" + f"""
 <table align="center" width="90%">
        <tr>
            <td><b>NAZWA FIRMY</b><br>
                Adres<br>
                Kod Pocztowy<br>
                tel: 111 222 333<br>
                adres@email.com
            </td>
            <td align="right"><img src="" alt="Logo" width="220" height="192"></td>
        </tr>
        <tr height="200">
            <td width="65%" style="font-size:26px"><b>Oferta NR:{oferta.id}</b><br>

            </td>
            <td>Oferta z dnia:{oferta.date}<br>
                Oferta ważna do:{oferta.date+ datetime.timedelta(days=14)}</td>
        </tr>
    </table>"""

    for element4 in oferta.element4:
        cenaZL1 = cenaZL1 + element4.cenaZL1
        cenaZL2 = cenaZL2 +  element4.cenaZL2
        wartosc_brutto = wartosc_brutto + int(round((1+element4.cenaZL2/100)*(element4.cenaZL2+element4.cenaZL1)))
        table = table+f"""
        <div class = "keep-together">
    <table class = "header" >
        <tr >
            <th rowspan = "2" class = "PosNumber" > <b > Poz.{index} </b > </th >
            <th > Cena 1 </th >
            <th > Wartość 1 </th >
            <th > Cena 2 </th >
            <th > Cena 3 </th >
            <th > Wartość 4</th >
        </tr >
        <tr >
            <td > {element4.cenaZL1}zł </td >
            <td > {element4.value1} </td >
            <td > {element4.cenaZL2}zł </td >
            <td > {element4.cenaZL3}% </td >
            <td > {int(round((1+element4.cenaZL3/100)*(element4.cenaZL2+element4.cenaZL1)))}zł </td >
        </tr>
    </table>
     <div class ="propertyHeader">
     Element 4:
     </div>
    <div class="property_container">
   
    <table class = "property ">

    """
        if element4.value1 != '':
            table=table +f"""

        <tr>
            <td>
                Wartość 1:
            </td>
            <td >
                {element4.value1}
            </td>
        </tr>
        """
        if element4.value2 != '':
            table=table +f"""

        <tr>
            <td>
                Wartość 2:
            </td>
            <td >
                {element4.value2}
            </td>
        </tr>
        """
        if element4.value3!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 3:
            </td>
            <td>
                {element4.value3}
            </td>
        </tr>"""
        if element4.value4!='':
            table = table+ f"""
        <tr>
            <td>
               Wartość 4:
            </td>
            <td>
                {element4.value4}
            </td>
        </tr>"""
        if element4.value5!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 5:
            </td>
            <td>
                {element4.value5}
            </td>
        </tr>"""
        if element4.value6!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 6:
            </td>
            <td>
                {element4.value6}
            </td>
        </tr>"""
        if element4.value7!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 7:
            </td>
            <td>
                {element4.value7}
            </td>
        </tr>"""
        if element4.value8!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 8:
            </td>
            <td>
                {element4.value8}
            </td>
        </tr>"""
        if element4.value9!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 9:
            </td>
            <td>
                {element4.value9}
            </td>
        </tr>"""
        if element4.value10!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 10:
            </td>
            <td>
                {element4.value10}
            </td>
        </tr>"""

                
        table = table+'</table>'
        if element4.dodatki != []:
            table = table+ f"""
            <h3> Dodatki</h3>
            <table class = "property_dodatki">
            <tr>
                <th>Ilość</th>
                <th>Element</th>
                <th>Wartość Netto</th>
            </tr>
            """
            for dodatki in element4.dodatki:
                table = table+ f"""
                        <tr>
            <td>
                {dodatki.value1}
            </td>
            <td>
                {dodatki.value2}
            </td>
                        <td>
                {dodatki.cenaZL2}zł
            </td>
                </tr>"""
            table = table+'</table>'   
         
        table = table+'</div></div>'
        index= index+1
    
    for element2 in oferta.element2:
        cenaZL1 = cenaZL1 + element2.cenaZL1
        cenaZL2 = cenaZL2 +  element2.cenaZL2
        wartosc_brutto = wartosc_brutto + int(round((1+element2.cenaZL2/100)*(element2.cenaZL2+element2.cenaZL1)))

        table = table+f"""
                <div class = "keep-together">

    <table class = "header" >
        <tr >
            <th rowspan = "2" class = "PosNumber" > <b > Poz.{index} </b > </th >
            <th > Montaż </th >
            <th > Ilość </th >
            <th > Wartość Netto </th >
            <th > cenaZL2 </th >
            <th > Wartość Brutto</th >
        </tr >
        <tr >
            <td > {element2.cenaZL1}zł </td >
            <td > {element2.value1} </td >
            <td > {element2.cenaZL2}zł </td >
            <td > {element2.cenaZL2}% </td >
            <td > {int(round((1+element2.cenaZL2/100)*(element2.cenaZL2+element2.cenaZL1)))}zł </td >
        </tr>
    </table>
    <div class ="propertyHeader">
     element2:
     </div>
    <div class="property_container">

    <table class = "property">
    """
        if element2.value2 != '':
            table=table +f"""

        <tr>
            <td>
                Wartość 2:
            </td>
            <td >
                {element2.value2}
            </td>
        </tr>
        """
        if element2.value3!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 3:
            </td>
            <td>
                {element2.value3}
            </td>
        </tr>"""
        if element2.value4!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 4:
            </td>
            <td>
                {element2.value4}
            </td>
        </tr>"""
        if element2.value5!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 5:
            </td>
            <td>
                {element2.value5}
            </td>
        </tr>"""
        if element2.value6!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 6:
            </td>
            <td>
                {element2.value6}
            </td>
        </tr>"""
        if element2.value7!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 7:
            </td>
            <td>
                {element2.value7}
            </td>
        </tr>"""
                        
        table = table+'</table>'
        if element2.dodatki != []:
            table = table+ f"""
            <h3> Dodatki</h3>
            <table class = "property_dodatki">
            <tr>
                <th>Ilość</th>
                <th>Element</th>
                <th>Wartość Netto</th>
            </tr>
            """
            for dodatki in element2.dodatki:
                table = table+ f"""
                        <tr>
            <td>
                {dodatki.value1}
            </td>
            <td>
                {dodatki.value2}
            </td>
                        <td>
                {dodatki.cenaZL2}zł
            </td>
                </tr>"""
            table = table+'</table>'   
      
        table = table+'</div> </div>'
        index= index+1



    for element5 in oferta.element5:
        cenaZL1 = cenaZL1 + element5.cenaZL1
        cenaZL2 = cenaZL2 +  element5.cenaZL2
        wartosc_brutto = wartosc_brutto + int(round((1+element5.cenaZL2/100)*(element5.cenaZL2+element5.cenaZL1)))      
        table = table+f"""
                <div class = "keep-together">

    <table class = "header" >
        <tr >
            <th rowspan = "2" class = "PosNumber" > <b > Poz.{index} </b > </th >
            <th > Montaż </th >
            <th > Ilość </th >
            <th > Wartość Netto </th >
            <th > cenaZL2 </th >
            <th > Wartość Brutto</th >
        </tr >
        <tr >
            <td > {element5.cenaZL1}zł </td >
            <td > {element5.value1} </td >
            <td > {element5.cenaZL2}zł </td >
            <td > {element5.cenaZL2}% </td >
            <td > {int(round((1+element5.cenaZL2/100)*(element5.cenaZL2+element5.cenaZL1)))}zł </td >
        </tr>
    </table>

    <div class ="propertyHeader">
     Element 5:
     </div>
    <div class="property_container">

    <table class = "property">
    """
        if element5.value1!= '':
            table=table +f"""

        <tr>
            <td>
                Wartość 1:
            </td>
            <td >
                {element5.value1}
            </td>
        </tr>
        """
        if element5.value2!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 2:
            </td>
            <td>
                {element5.value2}
            </td>
        </tr>"""
        if element5.value3!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 3:
            </td>
            <td>
                {element5.value3}
            </td>
        </tr>"""
        if element5.value4!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 4:
            </td>
            <td>
                {element5.value4}
            </td>
        </tr>"""
        if element5.value5!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 5:
            </td>
            <td>
                {element5.value5}
            </td>
        </tr>"""
        if element5.value6!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 6:
            </td>
            <td>
                {element5.value6}
            </td>
        </tr>"""
        if element5.value7!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 7:
            </td>
            <td>
                {element5.value7}
            </td>
        </tr>"""
        if element5.value9!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 8:
            </td>
            <td>
                {element5.value9}
            </td>
        </tr>"""
                        
        table = table+'</table>'
        if element5.dodatki != []:
            table = table+ f"""
            <h3> Dodatki</h3>
            <table class = "property_dodatki">
            <tr>
                <th>Ilość</th>
                <th>Element</th>
                <th>Wartość Netto</th>
            </tr>
            """
            for dodatki in element5.dodatki:
                table = table+ f"""
                        <tr>
            <td>
                {dodatki.value1}
            </td>
            <td>
                {dodatki.value2}
            </td>
                        <td>
                {dodatki.cenaZL2}zł
            </td>
                </tr>"""
            table = table+'</table>'   
        table = table+'</div></div>'
        index= index+1


    for element1 in oferta.element1:
        cenaZL1 = cenaZL1 + element1.cenaZL1
        cenaZL2 = cenaZL2 +  element1.cenaZL2
        wartosc_brutto = wartosc_brutto + int(round((1+element1.cenaZL2/100)*(element1.cenaZL2+element1.cenaZL1)))  
         
        table = table+f"""
                <div class = "keep-together">

    <table class = "header" >
        <tr >
            <th rowspan = "2" class = "PosNumber" > <b > Poz.{index} </b > </th >
            <th > Montaż </th >
            <th > Ilość </th >
            <th > Wartość Netto </th >
            <th > cenaZL2 </th >
            <th > Wartość Brutto</th >
        </tr >
        <tr >
            <td > {element1.cenaZL1}zł </td >
            <td > {element1.value1} </td >
            <td > {element1.cenaZL2}zł </td >
            <td > {element1.cenaZL2}% </td >
            <td > {int(round((1+element1.cenaZL2/100)*(element1.cenaZL2+element1.cenaZL1)))}zł </td >
        </tr>
    </table>
         <div class ="propertyHeader">
     element1:
     </div>
    <div class="property_container">

    <table class = "property">
    """
        if element1.value2!= '':
            table=table +f"""

        <tr>
            <td>
                Wartość 2:
            </td>
            <td >
                {element1.value2}
            </td>
        </tr>
        """
        if element1.value3!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 3:
            </td>
            <td>
                {element1.value3}
            </td>
        </tr>"""
        if element1.value4!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 4:
            </td>
            <td>
                {element1.value4}
            </td>
        </tr>"""
        if element1.value5!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 5:
            </td>
            <td>
                {element1.value5}
            </td>
        </tr>"""
        if element1.value6!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 6:
            </td>
            <td>
                {element1.value6}
            </td>
        </tr>"""
        if element1.value7!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 7:
            </td>
            <td>
                {element1.value7}
            </td>
        </tr>"""
        if element1.value8!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 8:
            </td>
            <td>
                {element1.value8}
            </td>
        </tr>"""
        
                        
        table = table+'</table>'
        if element1.dodatki != []:
            table = table+ f"""
            <h3> Dodatki</h3>
            <table class = "property_dodatki">
            <tr>
                <th>Ilość</th>
                <th>Element</th>
                <th>Wartość Netto</th>
            </tr>
            """
            for dodatki in element1.dodatki:
                table = table+ f"""
                        <tr>
            <td>
                {dodatki.value1}
            </td>
            <td>
                {dodatki.value2}
            </td>
                        <td>
                {dodatki.cenaZL2}zł
            </td>
                </tr>"""
            table = table+'</table>'   
       
        table = table+'</div></div>'
        index= index+1   

 
    for element3 in oferta.element3:
        cenaZL1 = cenaZL1 + element3.cenaZL1
        cenaZL2 = cenaZL2 +  element3.cenaZL2
        wartosc_brutto = wartosc_brutto + int(round((1+element3.cenaZL2/100)*(element3.cenaZL2+element3.cenaZL1)))  
 
        table = table+f"""
                <div class = "keep-together">

    <table class = "header" >
        <tr >
            <th rowspan = "2" class = "PosNumber" > <b > Poz.{index} </b > </th >
            <th > Montaż </th >
            <th > Ilość </th >
            <th > Wartość Netto </th >
            <th > cenaZL2 </th >
            <th > Wartość Brutto</th >
        </tr >
        <tr >
            <td > {element3.cenaZL1}zł </td >
            <td > {element3.value1} </td >
            <td > {element3.cenaZL2}zł </td >
            <td > {element3.cenaZL2}% </td >
            <td > {int(round((1+element3.cenaZL2/100)*(element3.cenaZL2+element3.cenaZL1)))}zł </td >
        </tr>
    </table>
         <div class ="propertyHeader">
     element3:
     </div>
    <div class="property_container">

    <table class = "property">
    """
        if element3.value2!= '':
            table=table +f"""

        <tr>
            <td>
                Wartość 2:
            </td>
            <td >
                {element3.value2}
            </td>
        </tr>
        """
        if element3.value3!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 3:
            </td>
            <td>
                {element3.value3}
            </td>
        </tr>"""
        if element3.value4!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 4:
            </td>
            <td>
                {element3.value4}
            </td>
        </tr>"""
        if element3.value5!='':
            table = table+ f"""
        <tr>
            <td>
                Wartość 5:
            </td>
            <td>
                {element3.value5}
            </td>
        </tr>"""
       
                        
        table = table+'</table>'
        if element3.dodatki != []:
            table = table+ f"""
            <h3> Dodatki</h3>
            <table class = "property_dodatki">
            <tr>
                <th>Ilość</th>
                <th>Element</th>
                <th>Wartość Netto</th>
            </tr>
            """
            for dodatki in element3.dodatki:
                table = table+ f"""
                        <tr>
            <td>
                {dodatki.value1}
            </td>
            <td>
                {dodatki.value2}
            </td>
                        <td>
                {dodatki.cenaZL2}zł
            </td>
                </tr>"""
            table = table+'</table>'   
             
        table = table+'</div></div>'
        index= index+1  
    table = table + f"""
                <div class = "keep-together">
    <table class = "header" >
        <tr >
            <th rowspan = "2" class = "PosNumber" > <b > Podsumowanie </b > </th >
            <th > Montaż </th >
            <th > Produkty Netto </th >
            <th > Wartość Brutto</th >
        </tr >
        <tr >
            <td > {cenaZL1}zł </td >
            <td > {cenaZL2}zł </td >
            <td > {wartosc_brutto}zł </td >
        </tr>
    </table>
"""
        
        

    table = table+"""</body >

</html >"""
    options = {
        'page-size': 'A4',
        'margin-top': '0.25in',
        'margin-right': '0.25in',
        'margin-bottom': '0.25in',
        'margin-left': '0.25in',
    }
    config = pdfkit.configuration(wkhtmltopdf=(os.getcwd()+r'\wkhtmltopdf\bin\wkhtmltopdf.exe'))
    pdfkit.from_string(table,path,configuration=config,options=options)
