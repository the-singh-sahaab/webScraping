{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import Counter \n",
    "\n",
    "\n",
    "file_path = r'p15_webscrap\\collected_file\\blackassign0001.txt'  # Replace with the path to your text file\n",
    "with open(file_path, 'r') as file:\n",
    "    content = file.read()\n",
    "# print(content)\n",
    "\n",
    "def count_words_fast(text):      \n",
    "    text = text.lower()      \n",
    "    skips = [\".\", \", \", \":\", \";\", \"'\", '\"', \"-\", \"\\n\", \"\\r\"]  \n",
    "    for ch in skips:  \n",
    "        text = text.replace(ch, \"\")  \n",
    "        # text = text.replace(\"\\n\", \"\").replace(\"\\r\", \"\") \n",
    "    word_counts = Counter(text.split(\" \"))  \n",
    "    return word_counts\n",
    "\n",
    "print(count_words_fast(content))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: nltk in c:\\users\\shubh\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (3.8.1)\n",
      "Requirement already satisfied: click in c:\\users\\shubh\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nltk) (8.1.3)\n",
      "Requirement already satisfied: joblib in c:\\users\\shubh\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nltk) (1.2.0)\n",
      "Requirement already satisfied: regex>=2021.8.3 in c:\\users\\shubh\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nltk) (2023.10.3)\n",
      "Requirement already satisfied: tqdm in c:\\users\\shubh\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nltk) (4.66.1)\n",
      "Requirement already satisfied: colorama in c:\\users\\shubh\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from click->nltk) (0.4.6)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 23.2.1 -> 23.3.2\n",
      "[notice] To update, run: C:\\Users\\shubh\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "!pip install nltk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading collection 'all'\n",
      "[nltk_data]    | \n",
      "[nltk_data]    | Downloading package abc to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package abc is already up-to-date!\n",
      "[nltk_data]    | Downloading package alpino to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package alpino is already up-to-date!\n",
      "[nltk_data]    | Downloading package averaged_perceptron_tagger to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package averaged_perceptron_tagger is already up-\n",
      "[nltk_data]    |       to-date!\n",
      "[nltk_data]    | Downloading package averaged_perceptron_tagger_ru to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package averaged_perceptron_tagger_ru is already\n",
      "[nltk_data]    |       up-to-date!\n",
      "[nltk_data]    | Downloading package basque_grammars to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package basque_grammars is already up-to-date!\n",
      "[nltk_data]    | Downloading package bcp47 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package bcp47 is already up-to-date!\n",
      "[nltk_data]    | Downloading package biocreative_ppi to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package biocreative_ppi is already up-to-date!\n",
      "[nltk_data]    | Downloading package bllip_wsj_no_aux to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package bllip_wsj_no_aux is already up-to-date!\n",
      "[nltk_data]    | Downloading package book_grammars to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package book_grammars is already up-to-date!\n",
      "[nltk_data]    | Downloading package brown to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package brown is already up-to-date!\n",
      "[nltk_data]    | Downloading package brown_tei to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package brown_tei is already up-to-date!\n",
      "[nltk_data]    | Downloading package cess_cat to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package cess_cat is already up-to-date!\n",
      "[nltk_data]    | Downloading package cess_esp to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package cess_esp is already up-to-date!\n",
      "[nltk_data]    | Downloading package chat80 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package chat80 is already up-to-date!\n",
      "[nltk_data]    | Downloading package city_database to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package city_database is already up-to-date!\n",
      "[nltk_data]    | Downloading package cmudict to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package cmudict is already up-to-date!\n",
      "[nltk_data]    | Downloading package comparative_sentences to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package comparative_sentences is already up-to-\n",
      "[nltk_data]    |       date!\n",
      "[nltk_data]    | Downloading package comtrans to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package comtrans is already up-to-date!\n",
      "[nltk_data]    | Downloading package conll2000 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package conll2000 is already up-to-date!\n",
      "[nltk_data]    | Downloading package conll2002 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package conll2002 is already up-to-date!\n",
      "[nltk_data]    | Downloading package conll2007 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package conll2007 is already up-to-date!\n",
      "[nltk_data]    | Downloading package crubadan to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package crubadan is already up-to-date!\n",
      "[nltk_data]    | Downloading package dependency_treebank to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package dependency_treebank is already up-to-date!\n",
      "[nltk_data]    | Downloading package dolch to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package dolch is already up-to-date!\n",
      "[nltk_data]    | Downloading package europarl_raw to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package europarl_raw is already up-to-date!\n",
      "[nltk_data]    | Downloading package extended_omw to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package extended_omw is already up-to-date!\n",
      "[nltk_data]    | Downloading package floresta to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package floresta is already up-to-date!\n",
      "[nltk_data]    | Downloading package framenet_v15 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package framenet_v15 is already up-to-date!\n",
      "[nltk_data]    | Downloading package framenet_v17 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package framenet_v17 is already up-to-date!\n",
      "[nltk_data]    | Downloading package gazetteers to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package gazetteers is already up-to-date!\n",
      "[nltk_data]    | Downloading package genesis to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package genesis is already up-to-date!\n",
      "[nltk_data]    | Downloading package gutenberg to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package gutenberg is already up-to-date!\n",
      "[nltk_data]    | Downloading package ieer to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package ieer is already up-to-date!\n",
      "[nltk_data]    | Downloading package inaugural to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package inaugural is already up-to-date!\n",
      "[nltk_data]    | Downloading package indian to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package indian is already up-to-date!\n",
      "[nltk_data]    | Downloading package jeita to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package jeita is already up-to-date!\n",
      "[nltk_data]    | Downloading package kimmo to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package kimmo is already up-to-date!\n",
      "[nltk_data]    | Downloading package knbc to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package knbc is already up-to-date!\n",
      "[nltk_data]    | Downloading package large_grammars to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package large_grammars is already up-to-date!\n",
      "[nltk_data]    | Downloading package lin_thesaurus to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package lin_thesaurus is already up-to-date!\n",
      "[nltk_data]    | Downloading package mac_morpho to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package mac_morpho is already up-to-date!\n",
      "[nltk_data]    | Downloading package machado to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package machado is already up-to-date!\n",
      "[nltk_data]    | Downloading package masc_tagged to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package masc_tagged is already up-to-date!\n",
      "[nltk_data]    | Downloading package maxent_ne_chunker to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package maxent_ne_chunker is already up-to-date!\n",
      "[nltk_data]    | Downloading package maxent_treebank_pos_tagger to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Package maxent_treebank_pos_tagger is already up-\n",
      "[nltk_data]    |       to-date!\n",
      "[nltk_data]    | Downloading package moses_sample to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping models\\moses_sample.zip.\n",
      "[nltk_data]    | Downloading package movie_reviews to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\movie_reviews.zip.\n",
      "[nltk_data]    | Downloading package mte_teip5 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\mte_teip5.zip.\n",
      "[nltk_data]    | Downloading package mwa_ppdb to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping misc\\mwa_ppdb.zip.\n",
      "[nltk_data]    | Downloading package names to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\names.zip.\n",
      "[nltk_data]    | Downloading package nombank.1.0 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    | Downloading package nonbreaking_prefixes to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\nonbreaking_prefixes.zip.\n",
      "[nltk_data]    | Downloading package nps_chat to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\nps_chat.zip.\n",
      "[nltk_data]    | Downloading package omw to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    | Downloading package omw-1.4 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    | Downloading package opinion_lexicon to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\opinion_lexicon.zip.\n",
      "[nltk_data]    | Downloading package panlex_swadesh to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    | Downloading package paradigms to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\paradigms.zip.\n",
      "[nltk_data]    | Downloading package pe08 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\pe08.zip.\n",
      "[nltk_data]    | Downloading package perluniprops to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping misc\\perluniprops.zip.\n",
      "[nltk_data]    | Downloading package pil to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\pil.zip.\n",
      "[nltk_data]    | Downloading package pl196x to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\pl196x.zip.\n",
      "[nltk_data]    | Downloading package porter_test to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping stemmers\\porter_test.zip.\n",
      "[nltk_data]    | Downloading package ppattach to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\ppattach.zip.\n",
      "[nltk_data]    | Downloading package problem_reports to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\problem_reports.zip.\n",
      "[nltk_data]    | Downloading package product_reviews_1 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\product_reviews_1.zip.\n",
      "[nltk_data]    | Downloading package product_reviews_2 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\product_reviews_2.zip.\n",
      "[nltk_data]    | Downloading package propbank to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    | Downloading package pros_cons to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\pros_cons.zip.\n",
      "[nltk_data]    | Downloading package ptb to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\ptb.zip.\n",
      "[nltk_data]    | Downloading package punkt to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping tokenizers\\punkt.zip.\n",
      "[nltk_data]    | Downloading package qc to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\qc.zip.\n",
      "[nltk_data]    | Downloading package reuters to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    | Downloading package rslp to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping stemmers\\rslp.zip.\n",
      "[nltk_data]    | Downloading package rte to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\rte.zip.\n",
      "[nltk_data]    | Downloading package sample_grammars to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping grammars\\sample_grammars.zip.\n",
      "[nltk_data]    | Downloading package semcor to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    | Downloading package senseval to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\senseval.zip.\n",
      "[nltk_data]    | Downloading package sentence_polarity to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\sentence_polarity.zip.\n",
      "[nltk_data]    | Downloading package sentiwordnet to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\sentiwordnet.zip.\n",
      "[nltk_data]    | Downloading package shakespeare to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\shakespeare.zip.\n",
      "[nltk_data]    | Downloading package sinica_treebank to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\sinica_treebank.zip.\n",
      "[nltk_data]    | Downloading package smultron to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\smultron.zip.\n",
      "[nltk_data]    | Downloading package snowball_data to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    | Downloading package spanish_grammars to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping grammars\\spanish_grammars.zip.\n",
      "[nltk_data]    | Downloading package state_union to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\state_union.zip.\n",
      "[nltk_data]    | Downloading package stopwords to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\stopwords.zip.\n",
      "[nltk_data]    | Downloading package subjectivity to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\subjectivity.zip.\n",
      "[nltk_data]    | Downloading package swadesh to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\swadesh.zip.\n",
      "[nltk_data]    | Downloading package switchboard to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\switchboard.zip.\n",
      "[nltk_data]    | Downloading package tagsets to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping help\\tagsets.zip.\n",
      "[nltk_data]    | Downloading package timit to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\timit.zip.\n",
      "[nltk_data]    | Downloading package toolbox to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\toolbox.zip.\n",
      "[nltk_data]    | Downloading package treebank to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\treebank.zip.\n",
      "[nltk_data]    | Downloading package twitter_samples to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\twitter_samples.zip.\n",
      "[nltk_data]    | Downloading package udhr to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\udhr.zip.\n",
      "[nltk_data]    | Downloading package udhr2 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\udhr2.zip.\n",
      "[nltk_data]    | Downloading package unicode_samples to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\unicode_samples.zip.\n",
      "[nltk_data]    | Downloading package universal_tagset to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping taggers\\universal_tagset.zip.\n",
      "[nltk_data]    | Downloading package universal_treebanks_v20 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    | Downloading package vader_lexicon to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    | Downloading package verbnet to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\verbnet.zip.\n",
      "[nltk_data]    | Downloading package verbnet3 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\verbnet3.zip.\n",
      "[nltk_data]    | Downloading package webtext to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\webtext.zip.\n",
      "[nltk_data]    | Downloading package wmt15_eval to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping models\\wmt15_eval.zip.\n",
      "[nltk_data]    | Downloading package word2vec_sample to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping models\\word2vec_sample.zip.\n",
      "[nltk_data]    | Downloading package wordnet to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    | Downloading package wordnet2021 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    | Downloading package wordnet2022 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\wordnet2022.zip.\n",
      "[nltk_data]    | Downloading package wordnet31 to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    | Downloading package wordnet_ic to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\wordnet_ic.zip.\n",
      "[nltk_data]    | Downloading package words to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\words.zip.\n",
      "[nltk_data]    | Downloading package ycoe to\n",
      "[nltk_data]    |     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]    |   Unzipping corpora\\ycoe.zip.\n",
      "[nltk_data]    | \n",
      "[nltk_data]  Done downloading collection all\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import nltk\n",
    "\n",
    "nltk.download('all')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting textblob\n",
      "  Downloading textblob-0.17.1-py2.py3-none-any.whl (636 kB)\n",
      "     -------------------------------------- 636.8/636.8 kB 1.1 MB/s eta 0:00:00\n",
      "Requirement already satisfied: nltk>=3.1 in c:\\users\\shubh\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from textblob) (3.8.1)\n",
      "Requirement already satisfied: click in c:\\users\\shubh\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nltk>=3.1->textblob) (8.1.3)\n",
      "Requirement already satisfied: joblib in c:\\users\\shubh\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nltk>=3.1->textblob) (1.2.0)\n",
      "Requirement already satisfied: regex>=2021.8.3 in c:\\users\\shubh\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nltk>=3.1->textblob) (2023.10.3)\n",
      "Requirement already satisfied: tqdm in c:\\users\\shubh\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from nltk>=3.1->textblob) (4.66.1)\n",
      "Requirement already satisfied: colorama in c:\\users\\shubh\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from click->nltk>=3.1->textblob) (0.4.6)\n",
      "Installing collected packages: textblob\n",
      "Successfully installed textblob-0.17.1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 23.2.1 -> 23.3.2\n",
      "[notice] To update, run: C:\\Users\\shubh\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "!pip install textblob"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to\n",
      "[nltk_data]     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n",
      "[nltk_data] Downloading package stopwords to\n",
      "[nltk_data]     C:\\Users\\shubh\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import nltk\n",
    "from nltk.tokenize import sent_tokenize, word_tokenize\n",
    "from nltk.corpus import stopwords\n",
    "from textblob import TextBlob  # Install using: pip install textblob\n",
    "nltk.download('punkt')\n",
    "nltk.download('stopwords')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'p15_webscrap\\\\collected_file\\\\blackassign0001.txt'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn [12], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;124;43mr\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mp15_webscrap\u001b[39;49m\u001b[38;5;124;43m\\\u001b[39;49m\u001b[38;5;124;43mcollected_file\u001b[39;49m\u001b[38;5;124;43m\\\u001b[39;49m\u001b[38;5;124;43mblackassign0001.txt\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mr\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mencoding\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mutf-8\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m file:\n\u001b[0;32m      2\u001b[0m     text \u001b[38;5;241m=\u001b[39m file\u001b[38;5;241m.\u001b[39mread()\n",
      "File \u001b[1;32m~\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages\\IPython\\core\\interactiveshell.py:282\u001b[0m, in \u001b[0;36m_modified_open\u001b[1;34m(file, *args, **kwargs)\u001b[0m\n\u001b[0;32m    275\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m}:\n\u001b[0;32m    276\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m    277\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIPython won\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m by default \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    278\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    279\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myou can use builtins\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m open.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    280\u001b[0m     )\n\u001b[1;32m--> 282\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mio_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfile\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'p15_webscrap\\\\collected_file\\\\blackassign0001.txt'"
     ]
    }
   ],
   "source": [
    "with open(r'p15_webscrap\\collected_file\\blackassign0001.txt', 'r', encoding='utf-8') as file:\n",
    "    text = file.read()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}