const fs = require('fs');
const path = require('path');

const htmlPath = path.join(__dirname, '..', 'graph.html');

if (!fs.existsSync(htmlPath)) {
    console.error("graph.html no encontrado.");
    process.exit(1);
}

let content = fs.readFileSync(htmlPath, 'utf8');

const newOptions = `var options = {
  autoResize: true,
  nodes: { 
    shape: 'dot', size: 20, font: { color: '#ffffff', size: 14, strokeWidth: 2, strokeColor: '#16213e' }, borderWidth: 1, borderWidthSelected: 3, shadow: { enabled: true, color: 'rgba(0,0,0,0.5)', size: 10, x: 5, y: 5 }
  },
  edges: {
    color: { color: '#4d5d78', highlight: '#ffb347', hover: '#8899aa' }, smooth: { type: 'continuous', roundness: 0.5 }, selectionWidth: 2.5
  },
  physics: { 
    enabled: true, barnesHut: { gravitationalConstant: -4000, centralGravity: 0.1, springLength: 200, springConstant: 0.04, damping: 0.09, avoidOverlap: 0.5 }, stabilization: { enabled: true, iterations: 200, updateInterval: 50 }
  },
  interaction: { hover: true, tooltipDelay: 200, navigationButtons: true, keyboard: true }
};`;

content = content.replace(/var options = \{[\s\S]*?\};/, newOptions);
content = content.replace(/background: #1a1a2e;/g, 'background: radial-gradient(circle at center, #24243e 0%, #1a1a2e 40%, #0f0c29 100%);');
content = content.replace(/background: #16213e;/g, 'background: rgba(22, 33, 62, 0.85); backdrop-filter: blur(5px);');
content = content.replace(/border: 1px solid #333;/g, 'border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 4px 15px rgba(0,0,0,0.5);');

fs.writeFileSync(htmlPath, content, 'utf8');
console.log("Estilos visuales aplicados con éxito a graph.html");
