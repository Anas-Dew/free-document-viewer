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
