#Nesting
capitals = {
  'France': 'Paris',
  'India': 'Dehli',
  'Germany': 'Berlin'
}

#Nesting a list in a Dictionary
travel_log = {
  'France': ['Paris', 'Lille', 'Dijon'],
  'German': {'Berlin', 'Hamburg', 'Stuttgart'}
}

#Nesting dictionary in dictionary
travel_log = {
  'France': {'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visits': 12},
  'Germany': {'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'], 'total_visits': 5}
}

#Nesting a dictionary in a list
travel_log = {
    {
      'country': 'France', 
      'cities_visited': ['Paris', 'Lille', 'Dijon'], 
      'total_visits': 12
    },
    {
      'country': 'Germany', 
      'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'], 
      'total_visits': 5
    }

}