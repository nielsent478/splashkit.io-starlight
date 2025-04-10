function applyTheme(theme) {
    for (const key in theme) {
      //Apply each color variable to the root of the document
      document.documentElement.style.setProperty(`--${key}`, theme[key]);
    }
  }
  
  //example
  //const darkTheme = {
    //'background-color': '#1e1e1e',
    //'text-color': '#ffffff',
    //'primary-color': '#3498db'
  //};
  
  //Call the function
 //applyTheme(darkTheme);
  