async function loadIntoTable(url, table){
    const tableBody = table.querySelector("tbody");
    const response = await fetch(url);
    const { data } = await response.json();

    tableBody.innerHTML = "";

    for (const item of data) {
        const rowElement = document.createElement("tr");

        const yearCellElement = document.createElement("td");
        const popCellElement = document.createElement("td");

        yearCellElement.textContent = item["Year"];
        popCellElement.textContent = item["Population"];

        rowElement.appendChild(yearCellElement);
        rowElement.appendChild(popCellElement);

        tableBody.appendChild(rowElement)
    }
}

loadIntoTable("https://datausa.io/api/data?drilldowns=Nation&measures=Population", document.querySelector("table"));