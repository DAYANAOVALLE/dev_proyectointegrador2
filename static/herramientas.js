const API = "https://dev-proyectointegrador2.onrender.com";

document.getElementById("herramientaForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const nombre = document.getElementById("nombre").value;
  const version = document.getElementById("version").value;
  const licencia = document.getElementById("licencia").value;

  await fetch(`${API}/herramientas`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre, version, licencia, activo: true })
  });

  cargarHerramientas();
  e.target.reset();
});

async function cargarHerramientas() {
  const res = await fetch(`${API}/herramientas`);
  const data = await res.json();
  const lista = document.getElementById("herramientaList");
  lista.innerHTML = "";
  data.forEach(h => {
    const li = document.createElement("li");
    li.textContent = `${h.nombre} v${h.version} - Licencia: ${h.licencia}`;
    lista.appendChild(li);
  });
}

async function buscarHerramienta() {
  const nombre = document.getElementById("searchTool").value;
  const res = await fetch(`${API}/herramientas/buscar?nombre=${nombre}`);
  const data = await res.json();
  const lista = document.getElementById("herramientaList");
  lista.innerHTML = "";
  if (data.length === 0) {
    lista.innerHTML = "<li>No se encontraron herramientas.</li>";
    return;
  }
  data.forEach(h => {
    const li = document.createElement("li");
    li.textContent = `${h.nombre} v${h.version} - Licencia: ${h.licencia}`;
    lista.appendChild(li);
  });
}
