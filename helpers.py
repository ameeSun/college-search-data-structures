def state_select(selected_state=None):
	states = [
		("", "Select"), ("AL", "Alabama"), ("AK", "Alaska"), ("AZ", "Arizona"), ("AR", "Arkansas"),
		("CA", "California"), ("CO", "Colorado"), ("CT", "Connecticut"), ("DE", "Delaware"),
		("DC", "District of Columbia"), ("FL", "Florida"), ("GA", "Georgia"), ("HI", "Hawaii"),
		("ID", "Idaho"), ("IL", "Illinois"), ("IN", "Indiana"), ("IA", "Iowa"),
		("KS", "Kansas"), ("KY", "Kentucky"), ("LA", "Louisiana"), ("ME", "Maine"),
		("MD", "Maryland"), ("MA", "Massachusetts"), ("MI", "Michigan"), ("MN", "Minnesota"),
		("MS", "Mississippi"), ("MO", "Missouri"), ("MT", "Montana"), ("NE", "Nebraska"),
		("NV", "Nevada"), ("NH", "New Hampshire"), ("NJ", "New Jersey"), ("NM", "New Mexico"),
		("NY", "New York"), ("NC", "North Carolina"), ("ND", "North Dakota"), ("OH", "Ohio"),
		("OK", "Oklahoma"), ("OR", "Oregon"), ("PA", "Pennsylvania"), ("RI", "Rhode Island"),
		("SC", "South Carolina"), ("SD", "South Dakota"), ("TN", "Tennessee"), ("TX", "Texas"),
		("UT", "Utah"), ("VT", "Vermont"), ("VA", "Virginia"), ("WA", "Washington"),
		("WV", "West Virginia"), ("WI", "Wisconsin"), ("WY", "Wyoming")
	]
	
	options = ""
	for abbreviation, state in states:
		selected = "selected" if abbreviation == selected_state else ""
		options += f'<option value="{abbreviation}" {selected}>{state}</option>'
	
	return options

def main_campus(checked=False):
	checkbox_html = 'Main Campus: <input type="checkbox" id="main" name="main"'
	if checked:
		checkbox_html += ' checked'
	checkbox_html += '>'
	return checkbox_html

def locale_select(locale=None):
	locales = [
		("", "Select"), 
		("11", "City: Large"), 
		("12", "City: Midsize"), 
		("13", "City: Small"), 
		("21", "Suburb: Large"),
		("22", "Suburb: Midsize"), 
		("23", "Suburb: Small"), 
		("31", "Town: Fringe"), 
		("32", "Town: Distant"),
		("33", "Town: Remote"), 
		("41", "Rural: Fringe"), 
		("42", "Rural: Distant"), 
		("43", "Rural: Remote")
	]
	
	options = ""
	for abbreviation, locale in locales:
		selected = "selected" if abbreviation == locale else ""
		options += f'<option value="{abbreviation}" {selected}>{locale}</option>'
	
	return options