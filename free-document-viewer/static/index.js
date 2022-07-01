/* A function that is called when the page is loaded. It is used to replace the URL with a blank
string. It is also used to get the text content of the dataframe and descframe elements and then
render them in the table-div-data and table-div-desc elements. */
window.onload = function () {
    history.replaceState("", "", "/");
    let datahtml = document.getElementById('dataframe').textContent;
    let tableid = document.getElementById('table-div-data');
    render_data = `${datahtml}`
    tableid.innerHTML = render_data;
    let deschtml = document.getElementById('descframe').textContent;
    let descid = document.getElementById('table-div-desc');
    render_desc = `${deschtml}`
    descid.innerHTML = render_desc;
};
