pageTemplate = """
    <html>
      <head>
        <style>
          table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
            padding: 5px;
            }
        </style>
      </head>
      <body>
        {0}
      </body>
    </html>"""

tableTemplate = """
    <table>
      <caption>{0}</caption>
      <tr>
        <th>Tail number</th>
        <th>Model number</th>
        <th>Model description</th>
        <th>Owner company name</th>
        <th>Company country code</th>
        <th>Company country name</th>
      </tr>
      {1}
    </table>"""

rowTemplate = """
    <tr style='background-color:{6}'>
      <td>{0}</td>
      <td>{1}</td>
      <td>{2}</td>
      <td>{3}</td>
      <td>{4}</td>
      <td>{5}</td>  
    </tr>"""

