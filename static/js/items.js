document.querySelector("#add-row").addEventListener("click", function (event) {
	event.preventDefault();
	const formset = document.querySelector("#id_item_set-TOTAL_FORMS");
	const newIndex = parseInt(formset.value);
	const row = document.createElement("tr");

	row.innerHTML = `
    <td><input type="number" step="0.01" value="1.00" name="item_set-${newIndex}-quantity" id="id_item_set-${newIndex}-quantity" class="quantity-input full-width"></td>
    <td><input type="text" name="item_set-${newIndex}-description" id="id_item_set-${newIndex}-description" class="description-input full-width"></td>
    <td><input type="number" step="0.01" value="0.00" name="item_set-${newIndex}-price" id="id_item_set-${newIndex}-price" class="price-input full-width"></td>
    <td class="total-item right-text"></td>
    <td><a href="#!" class="remove-row button red-bg white"><span class="material-icons">delete</span>Borrar</a></td>
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
			const formset = document.getElementById("id_item_set-TOTAL_FORMS");
			const numForms = parseInt(formset.value);
			formset.value = numForms - 1; // actualizar el número de formularios

			updateRows();
		}
	});

document.querySelector("#items").addEventListener("input", function (event) {
	if (
		event.target.classList.contains("quantity-input") ||
		event.target.classList.contains("price-input") ||
		event.target.id == "sub-total"
	) {
		const row = event.target.closest("tr");
		const quantity = parseFloat(row.querySelector(".quantity-input").value);
		const price = parseFloat(row.querySelector(".price-input").value);
		const total = quantity * price;
		row.querySelector(".total-item").textContent = total.toFixed(2);
	}
	updateRows();
});
function updateRows() {
	// Actualizar los índices en los nombres de los campos y la suma del total
	let subtotal = 0;
	const rows = document.querySelector("#items-formset").children;
	const discountField = document.querySelector("#discount");
	const subTotalElement = document.querySelector("#sub-total");
	const totalElement = document.querySelector("#total");

	for (let i = 0; i < rows.length; i++) {
		const row = rows[i];
		const quantityField = row.querySelector(".quantity-input");
		const descriptionField = row.querySelector(".description-input");
		const priceField = row.querySelector(".price-input");
		const totalItemField = row.querySelector(".total-item");

		quantityField.name = `item_set-${i}-quantity`;
		descriptionField.name = `item_set-${i}-description`;
		priceField.name = `item_set-${i}-price`;
		quantityField.id = `item_set-${i}-quantity`;
		descriptionField.id = `item_set-${i}-description`;
		priceField.id = `item_set-${i}-price`;
		// Actualizar totales de items
		const quantity = parseFloat(quantityField.value);
		const price = parseFloat(priceField.value);
		const totalItem = (quantity * price).toFixed(2);
		totalItemField.textContent = totalItem;
		subtotal += parseFloat(totalItem);
	}
	// Actualizar el total

	subTotalElement.textContent = parseFloat(subtotal).toFixed(2);
	totalElement.textContent = subtotal - parseFloat(discount.value);
}

function startCalc() {
	let bigTotal = 0;
	const rows = document.querySelector("#items-formset").children;
	for (let i = 0; i < rows.length; i++) {
		const row = rows[i];
		const quantity = parseFloat(row.querySelector(".quantity-input").value);
		const price = parseFloat(row.querySelector(".price-input").value);
		const total = quantity * price;
		row.querySelector(".total-item").textContent = total.toFixed(2);
		//Actualizar total
		bigTotal += parseFloat(total.toFixed(2));
	}
	// Actualizar el total
	const totalElement = document.querySelector("#total");
	totalElement.textContent = bigTotal.toFixed(2);
}
updateRows();
