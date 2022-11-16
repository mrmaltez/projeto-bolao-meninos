function createGame(player1, player2) {
    return `
    <li>
                <figure>
                    <img src="/static/img/icon=${player1}.svg" alt="Bandeira do ${player1}" />
                    <figcaption>${player1}</figcaption>
                </figure>
                <input class="heighttext" type="text" name='jogo_1_time_1'> <h3>x</h3> <input class="heighttext" type="text" name='jogo_1_time_2'> 
                <figure>
                    <img src="/static/img/icon=${player2}.svg" alt="Bandeira do ${player2}" />
                    <figcaption>${player2}</figcaption>
                </figure>
              </li>
    `
  }
  function createCard(date, day, games) {
    return `
    <div class="card">
            <h2>${date}<span>${day}</span></h2>
            <ul>
            ${games}
            </ul>
          </div>
    `
  }
  var jogos = { 'card_1':{
    'dia': '20/11',
    'dia_semana': 'Domingo',
    'jogos':{'jogo1': {'time1':'qatar',
                       'time2':'ecuador'}}
  },
  'card_2':{
    'dia': '21/11',
    'dia_semana': 'Segunda',
    'jogos':{'jogo1': {'time1':'england',
                       'time2':'iran'},
            'jogo2': {'time1':'senegal',
                       'time2':'netherlands'},
            'jogo3': {'time1':'united states',
                       'time2':'wales'},
                      }
  },
  'card_3':{
    'dia': '22/11',
    'dia_semana': 'Terça',
    'jogos':{'jogo1': {'time1':'argentina',
                       'time2':'saudi arabia'},
            'jogo2': {'time1':'denmark',
                       'time2':'tunisia'},
            'jogo3': {'time1':'mexico',
                       'time2':'poland'},
            'jogo4': {'time1':'france',
                       'time2':'australia'},
                      }
  },

  'card_4':{
    'dia': '23/11',
    'dia_semana': 'Quarta',
    'jogos':{'jogo1': {'time1':'morocco',
                       'time2':'croatia'},
            'jogo2': {'time1':'germany',
                       'time2':'japan'},
            'jogo3': {'time1':'spain',
                       'time2':'costa rica'},
            'jogo4': {'time1':'belgium',
                       'time2':'canada'},
                      }
  },

  'card_5':{
    'dia': '24/11',
    'dia_semana': 'Quinta',
    'jogos':{'jogo1': {'time1':'switzerland',
                       'time2':'cameroon'},
            'jogo2': {'time1':'uruguay',
                       'time2':'south korea'},
            'jogo3': {'time1':'portugal',
                       'time2':'ghana'},
            'jogo4': {'time1':'brazil',
                       'time2':'serbia'},
                      }
  },

  'card_6':{
    'dia': '25/11',
    'dia_semana': 'Sexta',
    'jogos':{'jogo1': {'time1':'wales',
                       'time2':'iran'},
            'jogo2': {'time1':'qatar',
                       'time2':'senegal'},
            'jogo3': {'time1':'netherlands',
                       'time2':'ecuador'},
            'jogo4': {'time1':'england',
                       'time2':'united states'},
                      }
  },

  'card_7':{
    'dia': '26/11',
    'dia_semana': 'Sábado',
    'jogos':{'jogo1': {'time1':'tunisia',
                       'time2':'australia'},
            'jogo2': {'time1':'poland',
                       'time2':'saudi arabia'},
            'jogo3': {'time1':'france',
                       'time2':'denmark'},
            'jogo4': {'time1':'argentina',
                       'time2':'mexico'},
                      }
  },
  'card_8':{
    'dia': '27/11',
    'dia_semana': 'Domingo',
    'jogos':{'jogo1': {'time1':'japan',
                       'time2':'costa rica'},
            'jogo2': {'time1':'belgium',
                       'time2':'morocco'},
            'jogo3': {'time1':'croatia',
                       'time2':'canada'},
            'jogo4': {'time1':'spain',
                       'time2':'germany'},
                      }
  },
  'card_9':{
    'dia': '28/11',
    'dia_semana': 'Segunda',
    'jogos':{'jogo1': {'time1':'cameroon',
                       'time2':'serbia'},
            'jogo2': {'time1':'south korea',
                       'time2':'ghana'},
            'jogo3': {'time1':'brazil',
                       'time2':'switzerland'},
            'jogo4': {'time1':'portugal',
                       'time2':'uruguay'},
                      }
  },

  'card_10':{
    'dia': '29/11',
    'dia_semana': 'Terça',
    'jogos':{'jogo1': {'time1':'ecuador',
                       'time2':'senegal'},
            'jogo2': {'time1':'netherlands',
                       'time2':'qatar'},
            'jogo3': {'time1':'iran',
                       'time2':'united states'},
            'jogo4': {'time1':'wales',
                       'time2':'england'},
                      }
  },
  'card_11':{
    'dia': '30/11',
    'dia_semana': 'Quarta',
    'jogos':{'jogo1': {'time1':'tunisia',
                       'time2':'france'},
            'jogo2': {'time1':'australia',
                       'time2':'denmark'},
            'jogo3': {'time1':'poland',
                       'time2':'argentina'},
            'jogo4': {'time1':'saudi arabia',
                       'time2':'mexico'},
                      }
  },
  'card_12':{
    'dia': '01/12',
    'dia_semana': 'Quinta',
    'jogos':{'jogo1': {'time1':'croatia',
                       'time2':'belgium'},
            'jogo2': {'time1':'canada',
                       'time2':'morocco'},
            'jogo3': {'time1':'japan',
                       'time2':'spain'},
            'jogo4': {'time1':'costa rica',
                       'time2':'germany'},
                      }
  },
  'card_13':{
    'dia': '02/12',
    'dia_semana': 'Sexta',
    'jogos':{'jogo1': {'time1':'south korea',
                       'time2':'portugal'},
            'jogo2': {'time1':'ghana',
                       'time2':'uruguay'},
            'jogo3': {'time1':'serbia',
                       'time2':'switzerland'},
            'jogo4': {'time1':'cameroon',
                       'time2':'brazil'},
                      }
  },

}

  function adjust_cards(jogos){
    var x = ''
    for (var card in jogos){
      x += `${createCard(jogos[card]['dia'],
      jogos[card]['dia_semana'],create_games(jogos[card]))}`

    }
    return x
  }

  function create_games(jogos){
    var games = ''
      for (var jogo in jogos['jogos']){
        games += `${createGame(jogos['jogos'][jogo]['time1'],
        jogos['jogos'][jogo]['time2'])}`
      }
    return games
  }

  document.querySelector('#cards').innerHTML = adjust_cards(jogos)

















  // `
  //     ${createCard('20/11', "Domingo",
  //       createGame('qatar', 'ecuador')
  //     )}
  //     ${createCard('21/11', "Segunda",
  //       createGame('england', '10:00', 'iran') +
  //       createGame('senegal', '13:00', 'netherlands') +
  //       createGame('united states', '16:00', 'wales')
  //     )}
  //     ${createCard('22/11', 'Terça',
  //       createGame('argentina', '07:00', 'saudi arabia') +
  //       createGame('denmark', '10:00', 'tunisia') +
  //       createGame('mexico', '13:00', 'poland') +
  //       createGame('france', '16:00', 'australia')
  //     )}
  //     ${createCard('23/11', 'Quarta',
  //       createGame('morocco', '07:00', 'croatia') +
  //       createGame('germany', '10:00', 'japan') +
  //       createGame('spain', '13:00', 'costa rica') +
  //       createGame('belgium', '16:00', 'canada')
  //     )}
  //     ${createCard('24/11', "Quinta",
  //       createGame('switzerland', '07:00', 'cameroon') +
  //       createGame('uruguay', '10:00', 'south korea') +
  //       createGame('portugal', '13:00', 'ghana') +
  //       createGame('brazil', '16:00', 'serbia')
  //     )}
  //     ${createCard('25/11', "Sexta",
  //       createGame('wales', '07:00', 'iran') +
  //       createGame('qatar', '10:00', 'senegal') +
  //       createGame('netherlands', '13:00', 'ecuador') +
  //       createGame('england', '16:00', 'united states')
  //     )}
  //     ${createCard('26/11', 'Sabado',
  //       createGame('tunisia', '07:00', 'australia') +
  //       createGame('poland', '10:00', 'saudi arabia') +
  //       createGame('france', '13:00', 'denmark') +
  //       createGame('argentina', '16:00', 'mexico')
  //     )}
  //     ${createCard('27/11', 'Domingo',
  //       createGame('japan', '07:00', 'costa rica') +
  //       createGame('belgium', '10:00', 'morocco') +
  //       createGame('croatia', '13:00', 'canada') +
  //       createGame('spain', '16:00', 'germany')
  //     )}
  //       ${createCard('28/11', 'Segunda',
  //         createGame('cameroon', '07:00', 'serbia') +
  //         createGame('south korea', '10:00', 'ghana') +
  //         createGame('brazil', '13:00', 'switzerland') +
  //         createGame('portugal', '16:00', 'uruguay')
  //       )}
  //       ${createCard('29/11', 'Terça',
  //         createGame('ecuador', '12:00', 'senegal') +
  //         createGame('netherlands', '12:00', 'qatar') +
  //         createGame('iran', '16:00', 'united states') +
  //         createGame('wales', '16:00', 'england')
  //       )}
  //       ${createCard('30/11', 'Quarta',
  //         createGame('tunisia', '12:00', 'france') +
  //         createGame('australia', '12:00', 'denmark') +
  //         createGame('poland', '16:00', 'argentina') +
  //         createGame('saudi arabia', '16:00', 'mexico')
  //       )}
  //       ${createCard('01/12', 'Quinta',
  //         createGame('croatia', '12:00', 'belgium') +
  //         createGame('canada', '12:00', 'morocco') +
  //         createGame('japan', '16:00', 'spain') +
  //         createGame('costa rica', '16:00', 'germany')
  //       )}
  //       ${createCard('02/12', 'Sexta',
  //         createGame('south korea', '12:00', 'portugal') +
  //         createGame('ghana', '12:00', 'uruguay') +
  //         createGame('serbia', '16:00', 'switzerland') +
  //         createGame('cameroon', '16:00', 'brazil')
  //       )}
  // `