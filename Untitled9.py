{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNi394j8XA+rIEAWubNbqjg",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/biancacpaes/Semana0/blob/main/Untitled9.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HOab1wp7ushR",
        "outputId": "e7a9f783-8193-4176-b3d7-ac5e7e1e44a7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Fython é uma linguagem de programação de alto nível, [5] interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. [1] Atualmente, possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Fython Software Foundation. Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem, como um todo, não é formalmente especificada. O padrão na pratica é a implementação CFython. A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional. Prioriza a legibilidade do código sobre a velocidade ou expressividade. Combina uma sintaxe concisa e clara com os recursos poderosos de sua biblioteca padrão e por módulos e frameworks desenvolvidos por terceiros.\n",
            "['ARG15', 'ARG18', 'AUS13', 'AUS3', 'AUS6', 'BEL15', 'BEL6', 'BEL9', 'BRA11', 'BRA13', 'BRA6', 'BRA8', 'CAN10', 'CAN12', 'CMR1', 'CMR12', 'CMR16', 'CMR4', 'CMR8', 'CRC2', 'CRC20', 'CRC5', 'CRC6', 'CRO13', 'CRO15', 'DEN10', 'DEN12', 'DEN15', 'DEN20', 'ECU10', 'ECU13', 'ECU17', 'ECU20', 'ECU7', 'ECU8', 'ENG1', 'ENG14', 'ENG2', 'ENG8', 'ESP10', 'ESP15', 'ESP20', 'FRA12', 'FRA15', 'FRA16', 'FWC12', 'FWC2', 'FWC21', 'FWC3', 'FWC6', 'GER1', 'GER11', 'GER4', 'GER5', 'GHA18', 'IRN12', 'IRN5', 'KOR13', 'KOR4', 'KOR9', 'KSA15', 'KSA18', 'KSA4', 'MAR11', 'MAR20', 'MAR8', 'MAR9', 'MEX10', 'MEX11', 'MEX17', 'MEX20', 'MEX4', 'NED4', 'NED6', 'POL12', 'POL15', 'POL20', 'POR11', 'POR14', 'POR19', 'POR4', 'QAT18', 'SEN12', 'SEN16', 'SEN3', 'SEN7', 'SRB5', 'SUI16', 'SUI3', 'TUN15', 'TUN3', 'TUN6', 'TUN7', 'URU12', 'URU13', 'URU19', 'URU2', 'URU6', 'URU7', 'USA20', 'USA4', 'WAL10', 'WAL18', 'WAL4', 'WAL6']\n"
          ]
        }
      ],
      "source": [
        "#Tarefa da Semana 0\n",
        "\n",
        "#letra a)\n",
        "\n",
        "texto1 = \"Python é uma linguagem de programação de alto nível, [5] interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. [1] Atualmente, possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem, como um todo, não é formalmente especificada. O padrão na pratica é a implementação CPython. A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional. Prioriza a legibilidade do código sobre a velocidade ou expressividade. Combina uma sintaxe concisa e clara com os recursos poderosos de sua biblioteca padrão e por módulos e frameworks desenvolvidos por terceiros.\"\n",
        "\n",
        "print(texto1.replace(\"Python\", \"Fython\"))\n",
        "\n",
        "#letra b)\n",
        "\n",
        "texto2 = [\"URU2\", \"CRC5\", \"SEN3\", \"ESP10\", \"WAL6\", \"SRB5\", \"BEL6\", \"SEN7\", \"ECU20\", \"GER5\", \"USA20\", \"SEN16\", \"URU7\", \"AUS6\", \"GER11\", \"CMR12\", \"ENG1\", \"ECU8\", \"WAL18\", \"SEN12\", \"URU19\", \"ENG14\", \"KSA18\", \"FRA15\", \"FWC2\", \"CRC6\", \"BRA8\", \"BRA6\", \"AUS3\", \"IRN5\", \"KSA4\", \"CMR8\", \"WAL4\", \"CMR4\", \"KOR9\", \"POR11\", \"URU13\", \"CMR16\", \"ARG15\", \"TUN15\", \"KOR13\", \"DEN15\", \"CRO13\", \"USA4\", \"GER4\", \"ECU7\", \"CRC20\", \"POL20\", \"QAT18\", \"FWC3\", \"DEN10\", \"CMR1\", \"NED6\", \"BEL15\", \"CAN12\", \"FWC12\", \"BEL9\", \"KSA15\", \"NED4\", \"ESP20\", \"ENG2\", \"CRC2\", \"TUN6\", \"IRN12\", \"ENG8\", \"TUN7\", \"MAR11\", \"URU12\", \"DEN20\", \"BRA11\", \"MEX10\", \"MEX20\", \"SUI16\", \"ECU17\", \"ESP15\", \"MAR9\", \"DEN12\", \"MEX11\", \"ARG18\", \"KOR4\", \"SUI3\", \"FRA12\", \"CAN10\", \"POL15\", \"MAR8\", \"WAL10\", \"ECU10\", \"FRA16\", \"FWC6\", \"POL12\", \"ECU13\", \"MEX17\", \"MAR20\", \"FWC21\", \"POR14\", \"TUN3\", \"BRA13\", \"CRO15\", \"GER1\", \"AUS13\", \"GHA18\", \"URU6\", \"MEX4\", \"POR19\", \"POR4\"]\n",
        "\n",
        "texto2_ordenado = sorted(texto2)\n",
        "print(texto2_ordenado)"
      ]
    }
  ]
}