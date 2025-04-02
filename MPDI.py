import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página (debe ser la primera llamada a Streamlit)
st.set_page_config(
    page_title="Metodología Proyectual de Diseño Industrial",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Información del autor (Texto en blanco)
st.markdown("""
<div style='background-color: #2D2D2D; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
    <h2 style='color: white;'>👤 Autor</h2>
    <p style='color: white;'>© 2025 <strong>Ibar Federico Anderson, Ph.D., Master, Industrial Designer</strong></p>
    <div style='display: flex; justify-content: space-between; margin-top: 10px;'>
        <div>
            <p style='color: white;'><img src="https://upload.wikimedia.org/wikipedia/commons/c/c7/Google_Scholar_logo.svg" style="height: 20px; vertical-align: middle;"> <a href="https://scholar.google.com/citations?user=mXD4RFUAAAAJ&hl=en" target="_blank" style='color: white;'>Google Scholar</a></p>
            <p style='color: white;'><img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg" style="height: 20px; vertical-align: middle;"> <a href="https://orcid.org/0000-0002-9732-3660" target="_blank" style='color: white;'>ORCID</a></p>
        </div>
        <div>
            <p style='color: white;'><img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/ResearchGate_icon_SVG.svg" style="height: 20px; vertical-align: middle;"> <a href="https://www.researchgate.net/profile/Ibar-Anderson" target="_blank" style='color: white;'>Research Gate</a></p>
            <p style='color: white;'><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" style="height: 20px; vertical-align: middle;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" style="height: 20px; vertical-align: middle;"> <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" style='color: white;'>CC BY 4.0 License</a></p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Encabezado de la aplicación
st.title("Metodología Proyectual de Diseño Industrial")
st.markdown("Un enfoque sistemático para el proceso de diseño industrial, visualizado mediante un diagrama de flujo con símbolos ISO.")

# HTML con el diagrama Mermaid y tooltips
html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metodología Proyectual de Diseño Industrial</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: white;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            width: 100%;
            max-width: 1900px;
            padding: 20px;
            box-sizing: border-box;
            position: relative;
        }
        
        /* Estilos para tooltips personalizados - Mejorados y ampliados */
        .custom-tooltip {
            position: fixed; /* Cambiado de 'absolute' a 'fixed' para mejor posicionamiento */
            background-color: rgba(0, 0, 0, 0.9);
            color: white;
            padding: 20px 25px; /* Aumentado el padding para más espacio interior */
            border-radius: 8px; /* Bordes más redondeados */
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.4); /* Sombra más visible */
            font-size: 16px; /* Tamaño de fuente aumentado */
            line-height: 1.6; /* Mayor espaciado entre líneas */
            max-width: 550px; /* Tooltip más ancho */
            min-width: 300px; /* Ancho mínimo */
            border: 2px solid rgba(255, 255, 255, 0.3); /* Borde más visible */
            z-index: 9999; /* Asegurar que esté por encima de todo */
            display: none;
            pointer-events: none;
            transition: opacity 0.3s, transform 0.2s;
            transform-origin: top left;
        }
        
        .custom-tooltip h3 {
            margin-top: 0;
            margin-bottom: 10px; /* Más espacio después del título */
            color: #ffb74d;
            border-bottom: 2px solid rgba(255, 255, 255, 0.3); /* Línea divisoria más visible */
            padding-bottom: 10px;
            font-size: 20px; /* Título más grande */
            font-weight: bold;
        }
        
        .custom-tooltip p {
            margin: 10px 0; /* Más espacio entre párrafos */
            letter-spacing: 0.3px; /* Ligero espaciado entre letras para mejor lectura */
        }
        
        /* Estilos específicos para los nodos del diagrama */
        .inicio circle {
            fill: #9ccc65;
            stroke: #7cb342;
            stroke-width: 1px;
        }
        .fase .label-container {
            fill: #90caf9;
            stroke: #2196f3;
            stroke-width: 1px;
        }
        .concepto .label-container {
            fill: #ffb74d;
            stroke: #ff9800;
            stroke-width: 1px;
        }
        .momento circle {
            fill: #f48fb1;
            stroke: #e91e63;
            stroke-width: 1px;
        }
        .decision .label-container {
            fill: #ffcccc;
            stroke: #cc0000;
            stroke-width: 1px;
        }
        .datos .label-container {
            fill: #ccffff;
            stroke: #008888;
            stroke-width: 1px;
        }
        .fin circle {
            fill: #9ccc65;
            stroke: #7cb342;
            stroke-width: 1px;
        }
        
        /* Estilos para hacer que los nodos se destaquen al pasar el ratón */
        .node:hover {
            filter: brightness(1.2);
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <div id="tooltip" class="custom-tooltip"></div>
        <pre class="mermaid">
        %%{
            init: {
                'theme': 'base',
                'themeVariables': {
                    'primaryColor': '#ffffff',
                    'primaryTextColor': '#000000',
                    'primaryBorderColor': '#ffffff',
                    'lineColor': '#ffffff',
                    'secondaryColor': '#ffffff',
                    'tertiaryColor': '#121212',
                    'fontSize': '20px', /* Aumentar tamaño de texto general */
                    'nodePadding': 15,  /* Más espacio alrededor de los nodos */
                    'nodeSpacing': 60   /* Más espacio entre nodos */
                }
            }
        }%%
        
        flowchart TD
            %% Definición de estilos
            classDef inicio fill:#9ccc65,stroke:#7cb342,stroke-width:1px
            classDef fase fill:#90caf9,stroke:#2196f3,stroke-width:1px
            classDef concepto fill:#ffb74d,stroke:#ff9800,stroke-width:1px
            classDef momento fill:#f48fb1,stroke:#e91e63,stroke-width:1px
            classDef decision fill:#ffcccc,stroke:#cc0000,stroke-width:1px
            classDef datos fill:#ccffff,stroke:#008888,stroke-width:1px
            classDef fin fill:#9ccc65,stroke:#7cb342,stroke-width:1px
            
            %% INICIO DEL PROCESO
            start([🏁 INICIO]) --> fase1([🔍 🏠 FASE 1: PREPARACIÓN E INVESTIGACIÓN])
            
            %% FASE 1
            fase1 --> A{{🏠 Observación y Empatía}}
            A -->|Identificación de necesidades| B[❓ Planteamiento del Problema]
            B --> C[(👨‍💻 💾 📲 🔗 Revisión del Estado del Arte)]
            
            %% TRANSICIÓN FASE 1 A FASE 2
            C --> fase2([💡 ✨ FASE 2: FORMULACIÓN Y CONCEPTUALIZACIÓN])
            
            %% FASE 2
            fase2 --> D[📑 Definición de Objetivos y Requisitos]
            D --> E{💡 Formulación de Hipótesis de Diseño}
            E -->|Hipótesis viable| F(💡 ✨ Ideación y Generación de Conceptos)
            E -->|Hipótesis no viable| B
            
            %% TRANSICIÓN FASE 2 A FASE 3
            F --> fase3([✏️ 🔨 FASE 3: DESARROLLO Y EXPERIMENTACIÓN])
            
            %% FASE 3
            fase3 --> G{✅ Selección y Desarrollo del Concepto}
            G -->|Concepto seleccionado| H[✏️ 📝 🎨 📐 Prototipado]
            G -->|Conceptos rechazados| F
            H --> I[(⚖️ 🔧 Diseño para Manufactura)]
            
            %% TRANSICIÓN FASE 3 A FASE 4
            I --> fase4([⚙️ 👤 FASE 4: VALIDACIÓN Y REFINAMIENTO])
            
            %% FASE 4
            fase4 --> J{{👤 Pruebas y Validación}}
            J --> K[⚙️ Análisis y Retroalimentación]
            K --> L{📑 ¿Cumple requisitos?}
            L -->|No| M((🔄 Ajustes))
            M --> H
            L -->|Sí| fase5
            
            %% FASE 5
            fase5([🚀 📢 FASE 5: IMPLEMENTACIÓN Y DIFUSIÓN]) --> N[(🏭 🔩 Industrialización y Documentación Técnica)]
            N --> O{{🚀 Lanzamiento y Seguimiento en el Mercado}}
            O --> P[📢 👪 👤 Generalización y Mejora Continua]
            
            %% FIN DEL PROCESO
            P --> end_([🎯 FIN])
            
            %% Ciclo de mejora continua
            P -.->|Nuevo ciclo| fase1
            
            %% Aplicación de estilos
            class start,end_ inicio
            class fase1,fase2,fase3,fase4,fase5 fase
            class A,O concepto
            class B,D,F,H,K,P momento
            class E,G,L decision
            class C,I,N datos
            class M fin
        </pre>
    </div>

    <script>
        // Configuración de Mermaid
        mermaid.initialize({
            startOnLoad: true,
            theme: 'default',
            securityLevel: 'loose',
            flowchart: {
                useMaxWidth: false,
                htmlLabels: true,
                curve: 'basis'
            },
            themeVariables: {
                fontSize: '18px', /* Tamaño de fuente aumentado en el diagrama */
                arrowheadColor: '#ffffff',
                lineColor: '#ffffff'
            }
        });
        
        // Datos para los tooltips
        const tooltipData = {
            'start': {
                title: '🏁 INICIO',
                content: 'Punto de inicio del proceso de diseño industrial. A partir de aquí comienza la metodología proyectual.'
            },
            'end_': {
                title: '🎯 FIN',
                content: 'Conclusión del proceso de diseño. Desde aquí puede iniciarse un nuevo ciclo de mejora continua.'
            },
            
            // Fases
            'fase1': {
                title: '🔍 🏠 FASE 1: PREPARACIÓN E INVESTIGACIÓN',
                content: 'Esta fase se enfoca en identificar necesidades, definir claramente el problema y explorar el contexto mediante la investigación del estado del arte.'
            },
            'fase2': {
                title: '💡 ✨ FASE 2: FORMULACIÓN Y CONCEPTUALIZACIÓN',
                content: 'Esta fase se centra en establecer los objetivos y requisitos del proyecto, formular las hipótesis de diseño y generar conceptos creativos para abordar el problema identificado.'
            },
            'fase3': {
                title: '✏️ 🔨 FASE 3: DESARROLLO Y EXPERIMENTACIÓN',
                content: 'Esta fase implica seleccionar y desarrollar el concepto más prometedor, crear prototipos y preparar el diseño para su futura manufactura.'
            },
            'fase4': {
                title: '⚙️ 👤 FASE 4: VALIDACIÓN Y REFINAMIENTO',
                content: 'Esta fase se enfoca en probar y validar el diseño, analizar los resultados y realizar ajustes para asegurar que el producto cumpla con todos los requisitos.'
            },
            'fase5': {
                title: '🚀 📢 FASE 5: IMPLEMENTACIÓN Y DIFUSIÓN',
                content: 'Esta fase final implica la preparación para la producción industrial, el lanzamiento al mercado y el establecimiento de procesos de mejora continua.'
            },
            
            // Elementos de cada fase
            'A': {
                title: '🏠 Observación y Empatía',
                content: 'Identificar necesidades, tendencias y problemas mediante la observación del entorno, estudios de usuarios, encuestas y análisis del mercado. Se fundamenta en la "observación curiosa" del MC14 y en la empatía del Design Thinking.'
            },
            'B': {
                title: '❓ Planteamiento del Problema',
                content: 'Definir claramente el problema de diseño industrial, estableciendo el alcance, las restricciones y las metas a alcanzar. Este paso equivale a "planteamiento del problema" en el método científico, adaptado a la realidad proyectual.'
            },
            'C': {
                title: '👨‍💻 💾 📲 🔗 Revisión del Estado del Arte',
                content: 'Investigar antecedentes, revisar literatura, analizar soluciones existentes, tecnologías y tendencias del mercado. Permite contextualizar la problemática y establecer un marco referencial robusto.'
            },
            'D': {
                title: '📑 Definición de Objetivos y Requisitos',
                content: 'Establecer las especificaciones funcionales, estéticas, ergonómicas, técnicas y de producción del producto. Se determinan los criterios de éxito y los indicadores de desempeño.'
            },
            'E': {
                title: '💡 Formulación de Hipótesis de Diseño',
                content: 'Plantear posibles soluciones o respuestas creativas al problema identificado, fundamentadas en teorías y datos recopilados. Esta "hipótesis de diseño" guiará la generación de ideas, similar a la fase de hipótesis en el método científico.'
            },
            'F': {
                title: '💡 ✨ Ideación y Generación de Conceptos',
                content: 'Realizar sesiones de brainstorming, bocetos, moodboards y aplicar técnicas como SCAMPER para explorar múltiples alternativas creativas. Se promueve la diversidad de ideas y se documentan las propuestas iniciales.'
            },
            'G': {
                title: '✅ Selección y Desarrollo del Concepto',
                content: 'Evaluar y filtrar las ideas generadas, seleccionando la o las propuestas más viables según criterios de innovación, factibilidad y alineación con los objetivos. Se profundiza en el concepto elegido, definiendo su modelo y estructura.'
            },
            'H': {
                title: '✏️ 📝 🎨 📐 Prototipado',
                content: 'Materializar el concepto a través de la creación de prototipos físicos o digitales (bocetos detallados, maquetas o modelos CAD). El prototipado permite visualizar, probar y ajustar la solución antes de invertir en la producción a gran escala.'
            },
            'I': {
                title: '⚖️ 🔧 Diseño para Manufactura (DFM)',
                content: 'Adaptar y optimizar el diseño para su producción, considerando costos, materiales, procesos industriales y normativas. Se establecen los lineamientos técnicos y se generan los planos y especificaciones finales.'
            },
            'J': {
                title: '👤 Pruebas y Validación',
                content: 'Realizar ensayos en laboratorio y pruebas de usuario que permitan medir la funcionalidad, ergonomía, seguridad y usabilidad del prototipo. Se aplican técnicas de análisis cuantitativo y cualitativo para contrastar la hipótesis de diseño.'
            },
            'K': {
                title: '⚙️ Análisis y Retroalimentación',
                content: 'Interpretar los resultados de las pruebas y recopilar feedback de usuarios y expertos, identificando oportunidades de mejora y ajustes necesarios. Esta iteración permite refinar la solución y validar su eficacia antes del escalado.'
            },
            'L': {
                title: '📑 ¿Cumple requisitos?',
                content: 'Punto de decisión donde se evalúa si el diseño cumple con todos los requisitos establecidos. Si no los cumple, se realizan ajustes y se regresa a la fase de prototipado.'
            },
            'M': {
                title: '🔄 Ajustes',
                content: 'Proceso de modificaciones y refinamientos al prototipo basado en los resultados de las pruebas y la retroalimentación recibida.'
            },
            'N': {
                title: '🏭 🔩 Industrialización y Documentación Técnica',
                content: 'Finalizar el diseño integrando los ajustes derivados de la validación, generando la documentación técnica necesaria para la producción en serie. Se preparan manuales, planos y especificaciones de manufactura que aseguren la reproducibilidad del producto.'
            },
            'O': {
                title: '🚀 Lanzamiento y Seguimiento en el Mercado',
                content: 'Implementar el proceso de producción, coordinar el lanzamiento y realizar un seguimiento post-venta que permita evaluar la aceptación y el desempeño del producto en el mercado. Se establecen mecanismos de retroalimentación continua para futuras mejoras.'
            },
            'P': {
                title: '📢 👪 👤 Generalización y Mejora Continua',
                content: 'Analizar la repetibilidad del proceso, la confiabilidad del diseño y su impacto en el campo industrial, sentando las bases para innovaciones futuras. Se fomenta la revisión por pares y la actualización del método, cerrando el ciclo y alimentando nuevos proyectos.'
            }
        };
        
        // Esperamos a que se cargue la página
        window.addEventListener('load', function() {
            // Función para inicializar los tooltips después de que Mermaid haya renderizado
            function initTooltips() {
                console.log('Intentando inicializar tooltips...');
                
                // Obtenemos el contenedor del tooltip
                const tooltip = document.getElementById('tooltip');
                
                if (!tooltip) {
                    console.error('No se pudo encontrar el elemento tooltip');
                    return;
                }
                
                // Seleccionamos todos los nodos del diagrama - usando una selección más amplia
                const allElements = document.querySelectorAll('g.node, .node, [id^="flowchart-"], svg g');
                
                if (allElements.length === 0) {
                    console.log('No se encontraron nodos en el diagrama, reintentando en 500ms...');
                    setTimeout(initTooltips, 500);
                    return;
                }
                
                console.log('Elementos encontrados: ' + allElements.length);
                
                // Función para procesar el ID del nodo y obtener la clave para tooltipData
                function getNodeKey(nodeId) {
                    return nodeId
                        .replace(/flowchart-\d+-/, '')  // Eliminar prefijos de flowchart-
                        .replace(/^flowchart-/, '')     // Eliminar prefijo flowchart- sin número
                        .replace(/^mermaid-\d+-/, '')   // Eliminar prefijos de mermaid-
                        .split('-')[0];                 // Tomar solo la primera parte (antes del primer guión)
                }
                
                // Procesar todos los elementos y agregar los eventos
                allElements.forEach(element => {
                    // Intentamos obtener el ID del nodo
                    let elementId = element.id || '';
                    
                    // Si no tiene ID, intentamos buscar un texto dentro que pueda ser usado como identificador
                    if (!elementId && element.textContent) {
                        const text = element.textContent.trim();
                        // Si el texto corresponde a alguna clave en tooltipData, usamos ese texto como ID
                        for (const key in tooltipData) {
                            if (text.includes(tooltipData[key].title)) {
                                elementId = key;
                                break;
                            }
                        }
                    }
                    
                    // Obtenemos la clave para tooltipData
                    const nodeKey = getNodeKey(elementId);
                    
                    console.log('Procesando elemento:', elementId, '-> Clave:', nodeKey);
                    
                    // Si encontramos datos para este nodo
                    if (tooltipData[nodeKey]) {
                        console.log('¡Datos de tooltip encontrados para ' + nodeKey + '!');
                        
                        // Agregamos evento mouseover
                        element.addEventListener('mouseover', function(e) {
                            e.stopPropagation(); // Evitar que el evento se propague
                            
                            // Creamos el contenido del tooltip
                            tooltip.innerHTML = `
                                <h3>${tooltipData[nodeKey].title}</h3>
                                <p>${tooltipData[nodeKey].content}</p>
                            `;
                            
                            // Posicionamos el tooltip cerca del cursor
                            tooltip.style.left = (e.clientX + 15) + 'px';
                            tooltip.style.top = (e.clientY + 15) + 'px';
                            
                            // Mostramos el tooltip
                            tooltip.style.display = 'block';
                            tooltip.style.opacity = '1';
                            
                            console.log('Mostrando tooltip para:', nodeKey);
                        });
                        
                        // Agregamos evento mouseout
                        element.addEventListener('mouseout', function(e) {
                            e.stopPropagation(); // Evitar que el evento se propague
                            
                            // Ocultamos el tooltip
                            tooltip.style.display = 'none';
                            console.log('Ocultando tooltip');
                        });
                        
                        // Agregamos evento para mover el tooltip con el cursor
                        element.addEventListener('mousemove', function(e) {
                            e.stopPropagation(); // Evitar que el evento se propague
                            
                            // Actualizamos la posición del tooltip
                            tooltip.style.left = (e.clientX + 15) + 'px';
                            tooltip.style.top = (e.clientY + 15) + 'px';
                        });
                    }
                });
                
                // También agregar un controlador global para el diagrama completo
                const diagram = document.querySelector('.mermaid');
                if (diagram) {
                    diagram.addEventListener('click', function(e) {
                        console.log('Diagrama clickeado en posición:', e.clientX, e.clientY);
                        console.log('Elemento target:', e.target.id || e.target.tagName);
                    });
                }
            }
            
            // Intentar inicializar varias veces para asegurar que Mermaid haya terminado de renderizar
            setTimeout(initTooltips, 1000);
            setTimeout(initTooltips, 2000);
            setTimeout(initTooltips, 3000);
        });
    </script>
</body>
</html>
"""

# Insertar el contenido HTML en la aplicación Streamlit
components.html(html_content, height=800, scrolling=True)

# Footer vacío
st.markdown("---")

# Añadir créditos y referencias
st.sidebar.title("Información")
st.sidebar.info("""
**Metodología Proyectual de Diseño Industrial**

Esta visualización interactiva representa un enfoque metodológico para el proceso de diseño industrial, 
combinando elementos del método científico, design thinking y metodologías ágiles adaptadas al contexto proyectual.

Pasa el cursor sobre los elementos del diagrama para ver descripciones detalladas de cada fase y actividad.
""")

st.sidebar.markdown("---")
st.sidebar.markdown("**Desarrollado con:**")
st.sidebar.markdown("- Streamlit")
st.sidebar.markdown("- Mermaid.js")
