const API_URL = "https://dev-proyectointegrador2.onrender.com";

document.addEventListener("DOMContentLoaded", listarHerramientas);

document.getElementById("formCrear").addEventListener("submit", async (e) => {
  e.preventDefault();

  const herramienta = {
    id: parseInt(document.getElementById("id").value),
    nombre: document.getElementById("nombre").value,
    version: document.getElementById("version").value,
    licencia: document.getElementById("licencia").value,
    activo: true
  };

  const res = await fetch(`${API_URL}/herramientas/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(herramienta)
  });

  if (res.ok) {
    listarHerramientas();
  } else {
    alert("Error al crear herramienta");
  }
});

async function listarHerramientas() {
  const res = await fetch(`${API_URL}/herramientas/`);
  const herramientas = await res.json();
  const lista = document.getElementById("listaHerramientas");
  lista.innerHTML = "";

  herramientas.forEach(h => {
    const li = document.createElement("li");
    li.innerHTML = `
      <strong>${h.nombre}</strong> (v${h.version}) - Licencia: ${h.licencia}
      <button onclick="eliminarHerramienta(${h.id})">Eliminar</button>
    `;
    lista.appendChild(li);
  });
}

async function buscarPorNombre() {
  const nombre = document.getElementById("buscarNombre").value;
  const res = await fetch(`${API_URL}/herramientas/buscar?nombre=${nombre}`);
  const herramientas = await res.json();
  mostrarResultados(herramientas);
}

async function filtrarPorLicencia() {
  const licencia = document.getElementById("filtroLicencia").value;
  const res = await fetch(`${API_URL}/herramientas/filtrar?licencia=${licencia}`);
  const herramientas = await res.json();
  mostrarResultados(herramientas);
}

function mostrarResultados(herramientas) {
  const lista = document.getElementById("listaHerramientas");
  lista.innerHTML = "";
  herramientas.forEach(h => {
    const li = document.createElement("li");
    li.innerHTML = `
      <strong>${h.nombre}</strong> (v${h.version}) - Licencia: ${h.licencia}
      <button onclick="eliminarHerramienta(${h.id})">Eliminar</button>
    `;
    lista.appendChild(li);
  });
}

async function eliminarHerramienta(id) {
  const res = await fetch(`${API_URL}/herramientas/${id}`, {
    method: "DELETE"
  });
  if (res.ok) {
    listarHerramientas();
  } else {
    alert("No se pudo eliminar");
  }
}
