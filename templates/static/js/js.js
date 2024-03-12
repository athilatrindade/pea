function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    
    return [bg_color, border_color];
    
}

function renderiza_total_consultas(url){  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('consultas_total').innerHTML = data.total
    })

}

function renderiza_total_consultas_atleta(url){  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('consultas_total').innerHTML = data.total
    })

}

function renderiza_total_testes(url){  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('testes_total').innerHTML = data.total
    })

}

function renderiza_total_testes_atleta(url){  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('testes_total').innerHTML = data.total
    })

}

function renderiza_angpopliteo_mensal(url) {
    const ctx = document.getElementById('angpopliteo_mensal').getContext('2d');
    var cores_despesas_mensal = gera_cor(qtd=12);

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {

        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao); 
            const valoresDireito = avaliacoes.map(item => parseFloat(item.direito)); 
            const valoresEsquerdo = avaliacoes.map(item => parseFloat(item.esquerdo)); 

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Direito',
                        data: valoresDireito,
                        backgroundColor: "#CB1EA8",
                        borderColor: "#000000",
                        borderWidth: 0.2
                    },
                    {
                        label: 'Esquerdo',
                        data: valoresEsquerdo,
                        backgroundColor: "#1E90FF",
                        borderColor: "#000000",
                        borderWidth: 0.2
                    }]
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('angpopliteo_mensal').style.display = 'none';
        }
    });
}

function renderiza_antropometria_mensal(url) {
    const ctx = document.getElementById('antropometria_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {

        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao); 
            const datasets = []; 

            
            const variaveis = ['Massacorporal', 'Altura', 'Dctriceps', 'Dcabdominal', 'Dcpanturrilha', 'Dcsubescapular', 'Circcoxamedial', 'Circpanturmedial', 'Dcbiceps', 'Dcpeitoral', 'Dccoxamedial', 'Dcsuprailiaca', 'Dccoxaproximal', 'Dcmedioaxilar'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('antropometria_mensal').style.display = 'none';
        }    
    });
}

function renderiza_calculoantropometria_mensal(url) {
    const ctx = document.getElementById('calculoantropometria_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {

        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao); 
            const datasets = []; 

            
            const variaveis = ['somanovedobras', 'somasetedobras', 'densicorporal', 'percgordural', 'imc', 'gordcorporal', 'massamagra'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
           
            console.log("Não há dados de avaliação para exibir o gráfico de Calculo Antropometria Mensal.");
            document.getElementById('calculoantropometria_mensal').style.display = 'none';
        }    
    });
}


function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}


function renderiza_compmembinf_mensal(url) {
    const ctx = document.getElementById('compmembinf_mensal').getContext('2d');
    var cores_despesas_mensal = gera_cor(qtd=12);

   
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {

        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao); 
            const valoresDireito = avaliacoes.map(item => parseFloat(item.direito)); 
            const valoresEsquerdo = avaliacoes.map(item => parseFloat(item.esquerdo));

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Direito',
                        data: valoresDireito,
                        backgroundColor: "#CB1EA8",
                        borderColor: "#000000",
                        borderWidth: 0.2
                    },
                    {
                        label: 'Esquerdo',
                        data: valoresEsquerdo,
                        backgroundColor: "#1E90FF",
                        borderColor: "#000000",
                        borderWidth: 0.2
                    }]
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('compmembinf_mensal').style.display = 'none';
        } 
    });
}

function renderiza_corrida_mensal(url) {
    const ctx = document.getElementById('corrida_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {

        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao); 
            const datasets = []; 

            const variaveis = ['tr', 'c20m', 'muddirecao', 'c10m', 'c30m', 'vift'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
           
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('corrida_mensal').style.display = 'none';
        }     
    });
}

function renderiza_desvam_mensal(url) {
    const ctx = document.getElementById('desvam_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {

        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao);
            const datasets = []; 

            
            const variaveis = ['c2km', 'c3km', 'vam'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('desvam_mensal').style.display = 'none';
        }      
    });
}

function renderiza_desempenhodesvam_mensal(url) {
    const ctx = document.getElementById('desempenhodesvam_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {

        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao);
            const datasets = []; 

            
            const variaveis = ['vam_2km', 'vam_3km'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Desempenho Desvam.");
            document.getElementById('desempenhodesvam_mensal').style.display = 'none';
        }      
    });
}

function renderiza_dorsiflexao_mensal(url) {
    const ctx = document.getElementById('dorsiflexao_mensal').getContext('2d');

   
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {

        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao);
            const datasets = []; 

            
            const variaveis = ['ec', 'dg', 'eg', 'dc'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('dorsiflexao_mensal').style.display = 'none';
        }     
    });
}

function renderiza_flexibilidade_mensal(url) {
    const ctx = document.getElementById('flexibilidade_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {

        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao);
            const datasets = [];

            
            const variaveis = ['wells_1', 'wells_2', 'wells_3'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('flexibilidade_mensal').style.display = 'none';
        }     
    });
}

function renderiza_maiorwellsflexibilidade_mensal(url) {
    const ctx = document.getElementById('maiorwellsflexibilidade_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {

        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao);
            const datasets = []; 

            
            const variaveis = ['maiorwells'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
           
            console.log("Não há dados de avaliação para exibir o gráfico de Maior Wells Flexibilidade.");
            document.getElementById('maiorwellsflexibilidade_mensal').style.display = 'none';
        }     
    });
}

function renderiza_fundtecnico_mensal(url) {
    const ctx = document.getElementById('fundtecnico_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        
        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao); 
            const datasets = []; 

            
            const variaveis = ['controle_1', 'controle_2', 'controle_3', 'passe_1', 'passe_2', 'passe_3', 'conducao_1', 'conducao_2', 'conducao_3', 'chute_1', 'chute_2', 'chute_3'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('fundtecnico_mensal').style.display = 'none';
        }  
    });
}

function renderiza_potmusmeminf_mensal(url) {
    const ctx = document.getElementById('potmusmeminf_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {

        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao);
            const datasets = []; 

            
            const variaveis = ['dj_1', 'dj_2', 'dj_3', 'sj_1', 'sj_2','sj_3','cmj_1','cmj_2','cmj_3'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('potmusmeminf_mensal').style.display = 'none';
        } 
    });
}

function renderiza_calculospotmusmeminf_mensal(url) {
    const ctx = document.getElementById('calculopotmusmeminf_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        
        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao);
            const datasets = []; 

            
            const variaveis = ['cmj_maior', 'sj_maior', 'dj_maior', 'indice_fr'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Cálculos potmusmeminf.");
            document.getElementById('calculopotmusmeminf_mensal').style.display = 'none';
        } 
    });
}

function renderiza_rast_mensal(url) {
    const ctx = document.getElementById('rast_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        
        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao);
            const datasets = []; 

           
            const variaveis = ['estimulo_1', 'estimulo_2', 'estimulo_3', 'estimulo_4', 'estimulo_5','estimulo_6'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('rast_mensal').style.display = 'none';
        }     
    });
}

function renderiza_calculorast_mensal(url) {
    const ctx = document.getElementById('calculorast_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        
        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao); 
            const datasets = []; 

            
            const variaveis = ['potanaerobia', 'capanaerobia', 'indfadiga'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Cálculo Rast.");
            document.getElementById('calculorast_mensal').style.display = 'none';
        }     
    });
}


function renderiza_runmatic_mensal(url) {
    const ctx = document.getElementById('runmatic_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        
        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

           
            const labels = avaliacoes.map(item => item.data_avaliacao); 
            const datasets = [];

            
            const variaveis = ['tcontatoesq', 'tcontatodir', 'tvooesq', 'tvoodir', 'freqpassadaesq','freqpassadadir','osverticalesq','osverticaldir','stifnessesq','stifnessdir','fmaximaesq','fmaximadir'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('runmatic_mensal').style.display = 'none';
        }     
    });
}

function renderiza_assimetriarunmatic_mensal(url) {
    const ctx = document.getElementById('assimetriarunmatic_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        
        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao);
            const datasets = []; 

            
            const variaveis = ['tcontato'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('assimetriarunmatic_mensal').style.display = 'none';
        }     
    });
}

function renderiza_testcadextensora_mensal(url) {
    const ctx = document.getElementById('testcadextensora_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
       
        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao); 
            const datasets = []; 

            
            const variaveis = ['direito', 'esquerdo'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('testcadextensora_mensal').style.display = 'none';
        }      
    });
}

function renderiza_testey_mensal(url) {
    const ctx = document.getElementById('testey_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        
        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao); 
            const datasets = []; 

            
            const variaveis = ['anterior_direito_1', 'anterior_direito_2', 'anterior_direito_3', 'anterior_esquerdo_1', 'anterior_esquerdo_2','anterior_esquerdo_3','postero_medial_dir_1','postero_medial_dir_2','postero_medial_dir_3','postero_medial_esq_1','postero_medial_esq_2','postero_medial_esq_3','postero_lat_esq_1','postero_lat_esq_2','postero_lat_esq_3','postero_lat_dir_1','postero_lat_dir_2','postero_lat_dir_3'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
           
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('testey_mensal').style.display = 'none';
        }     
    });
}

function renderiza_testmuscular_mensal(url) {
    const ctx = document.getElementById('testmuscular_mensal').getContext('2d');

   
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        
        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao); 
            const datasets = [];

            
            const variaveis = ['abduquadrildir', 'abduquadrilesq', 'rotquadrildir', 'rotquadrilesq', 'flexplantardir','flexplantaresq','flexjoelhodir','flexjoelhoesq','exjoelhodir','exjoelhoesq'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('testmuscular_mensal').style.display = 'none';
        }  
    });
}

function renderiza_testprogmaximo_mensal(url) {
    const ctx = document.getElementById('testprogmaximo_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        
        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao); 
            const datasets = []; 

            
            const variaveis = ['ultestatingido'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('testprogmaximo_mensal').style.display = 'none';
        }  
    });
}

function renderiza_testsalto_mensal(url) {
    const ctx = document.getElementById('testsalto_mensal').getContext('2d');

    
    fetch(url, {
        method: 'GET',
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        
        if (data.avaliacoes && data.avaliacoes.length > 0) {
            const avaliacoes = data.avaliacoes;

            // Processar os dados
            const labels = avaliacoes.map(item => item.data_avaliacao);
            const datasets = []; 

            
            const variaveis = ['direito','esquerdo'];

            for (let i = 0; i < variaveis.length; i++) {
                const variavel = variaveis[i];
                const valoresVariavel = avaliacoes.map(item => parseFloat(item[variavel.toLowerCase()]));

                datasets.push({
                    label: variavel,
                    data: valoresVariavel,
                    backgroundColor: getRandomColor(),
                    borderColor: "#000000",
                    borderWidth: 0.2
                });
            }

            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: datasets 
                },
            });
        } else {
            
            console.log("Não há dados de avaliação para exibir o gráfico de Angpopliteo.");
            document.getElementById('testsalto_mensal').style.display = 'none';
        }     
    });
}
