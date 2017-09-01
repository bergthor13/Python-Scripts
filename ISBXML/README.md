# ÍSB XML to CSV
This Python script takes the Excel file, for account overview, downloaded from [islandsbanki.is](http://www.islandsbanki.is) online bank and transforms it into a CSV file.

### File example

```html
<!DOCTYPE html>
<html>
<head>
	<!--[if gte mso 9]><xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet><x:Name>Yfirlit</x:Name><x:WorksheetOptions><x:Print><x:ValidPrinterInfo/></x:Print></x:WorksheetOptions></x:ExcelWorksheet></x:ExcelWorksheets></x:ExcelWorkbook></xml><![endif]-->
	<style>
	.Date { white-space:nowrap; mso-number-format:"Short Date"; }.Text { white-space:nowrap; mso-number-format:"\@"; }.Amount { white-space:nowrap; mso-number-format:"\#\,\#0"; }.Fixed { white-space:nowrap; mso-number-format:Fixed; }
	</style>
	<title></title>
</head>
<body>
	<meta content="text/html; charset=utf-8" http-equiv="Content-Type">
	<table>
		<tr>
			<th align="left" style="width:100px">Dags.</th>
			<th align="left" style="width:100px">Seðilnr.</th>
			<th align="left" style="width:100px">Textal.</th>
			<th align="left" style="width:100px">Tilvísun</th>
			<th align="left" style="width:100px">Skýring</th>
			<th align="right" style="width:100px">Hreyfing</th>
			<th align="right" style="width:100px">Staða</th>
		</tr>
		<tr>
			<td align="left" class="Date">01.09.2017</td>
			<td align="left" class="Text"></td>
			<td align="left" class="Text">MILLIF.</td>
			<td align="left" class="Text">0101910009</td>
			<td align="left" class="Text">Jón Jónsson</td>
			<td align="right" class="Amount" style="color:Red">-4000</td>
			<td align="right" class="Amount">30000</td>
		</tr>
		<tr>
			<td align="left" class="Date">01.09.2017</td>
			<td align="left" class="Text"></td>
			<td align="left" class="Text">MILLIF.</td>
			<td align="left" class="Text">0101910009</td>
			<td align="left" class="Text">Jón Jónsson</td>
			<td align="right" class="Amount">4000</td>
			<td align="right" class="Amount">34000</td>
		</tr>
	</table>
</body>
</html>
```