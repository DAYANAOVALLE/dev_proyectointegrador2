const API = "https://dev-proyectointegrador2.onrender.com";

document.getElementById("assetForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const nombre = document.getElementById("assetNombre").value;
  const tipo = document.getElementById("assetTipo").value;
  const autor = document.getElementById("assetAutor").value;
  const anio = parseInt(document.getElementById("assetAnio").value);

  await fetch(`${API}/assets`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre, tipo, autor, anio, activo: true })
  });

  cargarAssets();
  e.target.reset();
});

async function cargarAssets() {
  const res = await fetch(`${API}/assets`);
  const data = await res.json();
  const lista = document.getElementById("assetList");
  lista.innerHTML = "";
  data.forEach(asset => {
    const li = document.createElement("li");
    li.textContent = `${asset.nombre} (${asset.tipo}) - ${asset.anio} by ${asset.autor}`;
    lista.appendChild(li);
  });
}

async function buscarAsset() {
  const nombre = document.getElementById("searchNombre").value;
  const res = await fetch(`${API}/assets/buscar?nombre=${nombre}`);
  const data = await res.json();
  const lista = document.getElementById("assetList");
  lista.innerHTML = "";
  if (data.length === 0) {
    lista.innerHTML = "<li>No se encontraron assets.</li>";
    return;
  }
  data.forEach(asset => {
    const li = document.createElement("li");
    li.textContent = `${asset.nombre} (${asset.tipo}) - ${asset.anio} by ${asset.autor}`;
    lista.appendChild(li);
  });
}
