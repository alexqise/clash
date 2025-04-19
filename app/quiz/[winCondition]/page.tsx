"use client"

import { useState } from "react"
import Link from "next/link"
import Image from "next/image"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardFooter, CardHeader } from "@/components/ui/card"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import { Label } from "@/components/ui/label"
import { ChevronRight, Trophy, CheckCircle, XCircle } from "lucide-react"

interface QuizQuestion {
  question: string
  options: string[]
  correctAnswer: number
}

export default function QuizDetailPage({ params }: { params: { winCondition: string } }) {
  const [currentQuestion, setCurrentQuestion] = useState(0)
  const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null)
  const [isAnswered, setIsAnswered] = useState(false)
  const [score, setScore] = useState(0)
  const [quizCompleted, setQuizCompleted] = useState(false)

  // This would normally come from a database or API
  const quizData: Record<string, { name: string; questions: QuizQuestion[] }> = {
    "hog-rider": {
      name: "Hog Rider",
      questions: [
        {
          question: "Which building provides the best elixir trade against Hog Rider?",
          options: ["Inferno Tower", "Cannon", "Bomb Tower", "X-Bow"],
          correctAnswer: 1,
        },
        {
          question: "What is the optimal placement for a building to counter Hog Rider?",
          options: [
            "Directly in front of the tower",
            "4 tiles from the river in the center",
            "In the same lane as the Hog Rider, near the bridge",
            "Behind the Princess Tower",
          ],
          correctAnswer: 1,
        },
        {
          question: "Which spell can be used to activate the King Tower using a Hog Rider?",
          options: ["Fireball", "Zap", "Tornado", "Arrows"],
          correctAnswer: 2,
        },
        {
          question: "What happens if you place a Tombstone in the path of a Hog Rider?",
          options: [
            "Hog Rider jumps over it",
            "Hog Rider destroys it in one hit",
            "Hog Rider gets distracted and attacks it",
            "Hog Rider slows down but continues to the tower",
          ],
          correctAnswer: 2,
        },
        {
          question: "Which of these cards is NOT an effective counter to Hog Rider?",
          options: ["Mini P.E.K.K.A", "Skeleton Army", "Minion Horde", "Heal Spirit"],
          correctAnswer: 3,
        },
      ],
    },
    golem: {
      name: "Golem",
      questions: [
        {
          question: "What is the most effective strategy against a Golem placed in the back?",
          options: [
            "Defend with Inferno Tower immediately",
            "Push the opposite lane aggressively",
            "Save elixir and prepare a defense",
            "Place a tank killer in the back of your side",
          ],
          correctAnswer: 1,
        },
        {
          question: "Which card melts a Golem most efficiently?",
          options: ["P.E.K.K.A", "Inferno Dragon", "Sparky", "Elite Barbarians"],
          correctAnswer: 1,
        },
        {
          question: "What should you be most concerned about when defending against a Golem push?",
          options: [
            "The Golem itself",
            "The support troops behind the Golem",
            "The Golemites after the Golem dies",
            "The death damage",
          ],
          correctAnswer: 1,
        },
        {
          question: "Which spell is most effective against support troops behind a Golem?",
          options: ["Fireball", "Zap", "Poison", "Lightning"],
          correctAnswer: 2,
        },
        {
          question: "How much elixir does a Golem cost?",
          options: ["7 elixir", "8 elixir", "9 elixir", "10 elixir"],
          correctAnswer: 1,
        },
      ],
    },
    // Add more win conditions as needed
  }

  const winCondition = quizData[params.winCondition] || {
    name: "Unknown",
    questions: [
      {
        question: "No questions available for this win condition",
        options: ["Option 1", "Option 2", "Option 3", "Option 4"],
        correctAnswer: 0,
      },
    ],
  }

  const handleAnswerSelect = (index: number) => {
    if (!isAnswered) {
      setSelectedAnswer(index)
    }
  }

  const handleSubmitAnswer = () => {
    if (selectedAnswer === null) return

    setIsAnswered(true)

    if (selectedAnswer === winCondition.questions[currentQuestion].correctAnswer) {
      setScore(score + 1)
    }
  }

  const handleNextQuestion = () => {
    if (currentQuestion < winCondition.questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1)
      setSelectedAnswer(null)
      setIsAnswered(false)
    } else {
      setQuizCompleted(true)
    }
  }

  const resetQuiz = () => {
    setCurrentQuestion(0)
    setSelectedAnswer(null)
    setIsAnswered(false)
    setScore(0)
    setQuizCompleted(false)
  }

  return (
    <div className="flex flex-col min-h-screen">
      {/* Header */}
      <header className="bg-blue-900 text-white shadow-md">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <Trophy className="h-8 w-8 text-yellow-400" />
            <h1 className="text-xl md:text-2xl font-bold">Clash Counter Academy</h1>
          </div>
          <nav className="hidden md:flex gap-6">
            <Link href="/" className="hover:text-yellow-400 font-medium">
              Home
            </Link>
            <Link href="/learn" className="hover:text-yellow-400 font-medium">
              Learn
            </Link>
            <Link href="/quiz" className="hover:text-yellow-400 font-medium">
              Quiz
            </Link>
            <Link href="/about" className="hover:text-yellow-400 font-medium">
              About
            </Link>
          </nav>
          <Button variant="outline" className="md:hidden bg-transparent border-white text-white hover:bg-blue-800">
            Menu
          </Button>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-grow bg-gray-50">
        <div className="container mx-auto px-4 py-8">
          <div className="flex items-center gap-2 mb-6">
            <Link href="/" className="text-blue-600 hover:underline">
              Home
            </Link>
            <ChevronRight className="h-4 w-4" />
            <Link href="/quiz" className="text-blue-600 hover:underline">
              Quiz
            </Link>
            <ChevronRight className="h-4 w-4" />
            <span>{winCondition.name}</span>
          </div>

          {!quizCompleted ? (
            <Card className="max-w-3xl mx-auto">
              <CardHeader>
                <div className="flex justify-between items-center mb-4">
                  <h1 className="text-2xl font-bold">{winCondition.name} Quiz</h1>
                  <div className="text-sm font-medium">
                    Question {currentQuestion + 1} of {winCondition.questions.length}
                  </div>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2.5">
                  <div
                    className="bg-blue-600 h-2.5 rounded-full"
                    style={{ width: `${((currentQuestion + 1) / winCondition.questions.length) * 100}%` }}
                  ></div>
                </div>
              </CardHeader>
              <CardContent>
                <div className="mb-6">
                  <h2 className="text-xl font-medium mb-4">{winCondition.questions[currentQuestion].question}</h2>
                  <RadioGroup value={selectedAnswer?.toString() || ""} className="space-y-3">
                    {winCondition.questions[currentQuestion].options.map((option, index) => (
                      <div
                        key={index}
                        className={`
                          flex items-center space-x-2 rounded-lg border p-4 cursor-pointer
                          ${selectedAnswer === index ? "bg-blue-50 border-blue-200" : ""}
                          ${
                            isAnswered && index === winCondition.questions[currentQuestion].correctAnswer
                              ? "bg-green-50 border-green-200"
                              : ""
                          }
                          ${
                            isAnswered &&
                            selectedAnswer === index &&
                            index !== winCondition.questions[currentQuestion].correctAnswer
                              ? "bg-red-50 border-red-200"
                              : ""
                          }
                        `}
                        onClick={() => handleAnswerSelect(index)}
                      >
                        <RadioGroupItem
                          value={index.toString()}
                          id={`option-${index}`}
                          disabled={isAnswered}
                          className="sr-only"
                        />
                        <Label htmlFor={`option-${index}`} className="flex-grow cursor-pointer">
                          {option}
                        </Label>
                        {isAnswered && index === winCondition.questions[currentQuestion].correctAnswer && (
                          <CheckCircle className="h-5 w-5 text-green-500" />
                        )}
                        {isAnswered &&
                          selectedAnswer === index &&
                          index !== winCondition.questions[currentQuestion].correctAnswer && (
                            <XCircle className="h-5 w-5 text-red-500" />
                          )}
                      </div>
                    ))}
                  </RadioGroup>
                </div>
              </CardContent>
              <CardFooter className="flex justify-between">
                {!isAnswered ? (
                  <Button onClick={handleSubmitAnswer} disabled={selectedAnswer === null} className="w-full">
                    Submit Answer
                  </Button>
                ) : (
                  <Button onClick={handleNextQuestion} className="w-full">
                    {currentQuestion < winCondition.questions.length - 1 ? "Next Question" : "See Results"}
                  </Button>
                )}
              </CardFooter>
            </Card>
          ) : (
            <Card className="max-w-3xl mx-auto text-center">
              <CardHeader>
                <h1 className="text-2xl font-bold mb-2">Quiz Completed!</h1>
                <p className="text-gray-600">
                  You scored {score} out of {winCondition.questions.length}
                </p>
              </CardHeader>
              <CardContent>
                <div className="mb-6">
                  <div className="relative h-48 w-48 mx-auto mb-4">
                    <Image
                      src={`/placeholder.svg?height=192&width=192&text=${encodeURIComponent(
                        score === winCondition.questions.length
                          ? "Perfect Score!"
                          : score >= winCondition.questions.length / 2
                            ? "Good Job!"
                            : "Keep Learning!",
                      )}`}
                      alt="Quiz result"
                      fill
                      className="object-contain"
                    />
                  </div>

                  <p className="text-lg">
                    {score === winCondition.questions.length
                      ? "Perfect! You're a master at countering " + winCondition.name + "!"
                      : score >= winCondition.questions.length / 2
                        ? "Good job! You know how to counter " + winCondition.name + " pretty well."
                        : "Keep practicing! Countering " + winCondition.name + " takes some practice."}
                  </p>
                </div>
              </CardContent>
              <CardFooter className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button onClick={resetQuiz} variant="outline">
                  Retake Quiz
                </Button>
                <Button asChild>
                  <Link href={`/learn/${params.winCondition}`}>Review {winCondition.name} Counters</Link>
                </Button>
                <Button asChild variant="outline">
                  <Link href="/quiz">Try Another Quiz</Link>
                </Button>
              </CardFooter>
            </Card>
          )}
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8">
        <div className="container mx-auto px-4">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="flex items-center gap-2 mb-4 md:mb-0">
              <Trophy className="h-6 w-6 text-yellow-400" />
              <span className="text-lg font-bold">Clash Counter Academy</span>
            </div>
            <div className="flex gap-6">
              <Link href="/" className="hover:text-yellow-400">
                Home
              </Link>
              <Link href="/learn" className="hover:text-yellow-400">
                Learn
              </Link>
              <Link href="/quiz" className="hover:text-yellow-400">
                Quiz
              </Link>
              <Link href="/about" className="hover:text-yellow-400">
                About
              </Link>
            </div>
          </div>
          <div className="mt-6 text-center md:text-left text-gray-400 text-sm">
            <p>© {new Date().getFullYear()} Clash Counter Academy. Not affiliated with Supercell.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
