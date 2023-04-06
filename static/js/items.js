document
.getElementById("add-row")
.addEventListener("click", function (event) {
    event.preventDefault();
    const formset = document.getElementById("id_item_set-TOTAL_FORMS");
    const newIndex = parseInt(formset.value);
    const row = document.createElement("tr");
    row.innerHTML = `
    <td><input type="number" name="item_set-${newIndex}-quantity" id="id_item_set-${newIndex}-quantity" class="quantity-input"></td>
    <td><input type="text" name="item_set-${newIndex}-description" id="id_item_set-${newIndex}-description" class="description-input"></td>
    <td><input type="number" name="item_set-${newIndex}-price" id="id_item_set-${newIndex}-price" class="price-input"></td>
    <td><span class="total-span">0</span></td>
    <td><a href="#!" class="remove-row button red-bg white"><i class="material-icons">delete</i>Borrar</a></td>
    `;
    document.querySelector("#item-table tbody").appendChild(row);
    formset.value = newIndex + 1; // actualizar el número de formularios
    updateRows();
});

document
.querySelector("#item-table tbody")
.addEventListener("click", function (event) {
    if (event.target.classList.contains("remove-row")) {
        event.preventDefault();
        event.target.closest("tr").remove();
        const formset = document.getElementById(
            "id_item_set-TOTAL_FORMS"
        );
        const numForms = parseInt(formset.value);
        formset.value = numForms - 1; // actualizar el número de formularios

        updateRows();
    }
});

document
.querySelector("#item-table tbody")
.addEventListener("input", function (event) {
    if (
        event.target.classList.contains("quantity-input") ||
        event.target.classList.contains("price-input")
    ) {
        const row = event.target.closest("tr");
        const quantity = parseFloat(
            row.querySelector(".quantity-input").value
        );
        const price = parseFloat(
            row.querySelector(".price-input").value
        );
        const total = quantity * price;
        row.querySelector(".total-span").textContent = total.toFixed(2);
    }
    updateRows();
});
function updateRows() {
// Actualizar los índices en los nombres de los campos
const rows = document.querySelector("#items-formset").children;
for (let i = 0; i < rows.length; i++) {
    const quantityField = rows[i].querySelector(".quantity-input");
    const descriptionField =
        rows[i].querySelector(".description-input");
    const priceField = rows[i].querySelector(".price-input");

    quantityField.name = `item_set-${i}-quantity`;
    descriptionField.name = `item_set-${i}-description`;
    priceField.name = `item_set-${i}-price`;
    quantityField.id = `item_set-${i}-quantity`;
    descriptionField.id = `item_set-${i}-description`;
    priceField.id = `item_set-${i}-price`;
}
}